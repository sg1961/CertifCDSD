import time
import os

import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from picamera2 import Picamera2
import cv2
from model_3 import warm as cnn_warm, predict as ncnn_predict
import numpy as np

# Global variable to store the latest frame
frame = None

def capture_frames(save_stream=False):
    """
    Captures frames from Picamera2 and updates the global frame variable.
    """
    global frame
    camera = Picamera2()

    # Default
    # camera_config = camera.create_still_configuration(main={"size": (640, 480)})

    # Seddik
    #picam2.set_controls({"ExposureTime": 10000})  # Ajuster le temps d'exposition )
    camera_config = camera.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})

    fps = 5.0
    camera.controls.FrameRate = fps
    # camera_config = camera.create_preview_configuration(main={"size": (640, 480)})

    camera.configure(camera_config)
    camera.start()

    video_writer = None

    if save_stream:
      save_dir = os.getenv('DSFS_FT_31_SAVE_BASE_DIR', '/app/dump')
      output_video_filename = f"inference_stream_{time.strftime('%Y%m%d_%H%M%S')}.avi"
      
      # Define the directory containing your images relative to the script location
      output_video_path = os.path.join(save_dir, output_video_filename)
      
      print(f"Generated filename: {output_video_path}")
      fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use 'XVID' or 'MJPG' for .avi files
      video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (640, 480))

    try:
        while True:
            # raw_frame = np.array(camera.capture_buffer()).reshape(480, 640, 3)
            
            raw_frame = camera.capture_array()
            predicted = ncnn_predict(raw_frame)
            # predicted = seddik_predict(raw_frame)
            frame = predicted['image']
            
            if video_writer:
              video_writer.write(frame)

            # time.sleep(0.033)  # 30 FPS
    finally:
        if video_writer:    
          video_writer.release()
        camera.stop()

class StreamingHandler(BaseHTTPRequestHandler):
    """
    HTTP handler to serve a basic index page and stream MJPEG frames.
    """
    def do_GET(self):
        if self.path == '/':
            # Serve a simple HTML page with a video element
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Camera Stream</title>
                </head>
                <body>
                    <h1>Welcome to the Camera Stream</h1>
                    <p>View the live stream below:</p>
                    <img src="/rpi-eye" />
                </body>
                </html>
            """)
        elif self.path == '/rpi-eye':
            # Serve the MJPEG stream
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            while True:
                if frame is not None:
                    ret, jpeg = cv2.imencode('.jpg', frame)
                    if ret:
                        self.wfile.write(b'--frame\r\n')
                        self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
                        self.wfile.write(jpeg.tobytes())
                        self.wfile.write(b'\r\n')
                    time.sleep(0.033)  # Adjust as needed for your desired FPS
        else:
            # Handle unknown paths with a 404 error
            self.send_error(404)
            self.end_headers()

def start_http_server():
    """
    Starts the HTTP server.
    """
    server = HTTPServer(('0.0.0.0', 5000), StreamingHandler)
    server.serve_forever()

if __name__ == "__main__":
    save_stream = os.getenv('DSFS_FT_31_SAVE_STREAM', 'false') == 'true'
    if save_stream:
      print('Inference stream will be saved')
    
    cnn_warm()
    # Create threads for capture and HTTP server
    capture_thread = threading.Thread(target=capture_frames, daemon=True, args=(save_stream,))
    http_thread = threading.Thread(target=start_http_server, daemon=True)

    # Start threads
    capture_thread.start()
    http_thread.start()

    # Keep the main thread alive
    capture_thread.join()
    http_thread.join()
