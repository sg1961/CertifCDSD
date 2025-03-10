import os
import cv2
import time

from model_1 import predict as predict_model_1
from model_5 import predict as predict_model_5
from model_6 import predict as predict_model_6

DATASETS_BASE_DIR=os.environ.get('DSFS_FT_31_DATASETS_BASE_DIR').strip('"')

print('Reading datasets from: ', DATASETS_BASE_DIR)

# import math
# import time
# start webcam

# cap = cv2.VideoCapture(0)

# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)

#     # write the flipped frame
#     out.write(frame)

#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()

# cap = cv2.VideoCapture('c:/Users/cguillot/OneDrive/Work/jedha-dsfs-ft-31-final-project/data/raw/Harley-Davidson Breakout Morning Ride ｜ Pure Engine Sound [mXS_Syt7CGA].mp4')
VIDEOS = [f'{DATASETS_BASE_DIR}/raw/video/Monfilm2.mp4', f'{DATASETS_BASE_DIR}/raw/video/Monfilm3.mp4', f'{DATASETS_BASE_DIR}/raw/video/Rpivideo_7.mp4']
# video_path = f'{DATASETS_BASE_DIR}/raw/video/Monfilm3.mp4'
video_index = 0
video_path = VIDEOS[video_index]
output_filename = 'output_video_1.mp4'

crop_center_zone = video_index in [0, 1]

model_id = 1

if model_id == 1:
    predict_callable = predict_model_1
if model_id == 5:
    predict_callable = predict_model_5
elif model_id == 6:
    predict_callable = predict_model_6
else:
    print('UNKNOWN MODEL')

# Model 6
out_frame_width = 640
out_frame_height = 640


print('Viewing ', video_path)
cap = cv2.VideoCapture(video_path)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# Get video properties
# frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Should be 1280
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Should be 720

fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30  # Use 30 FPS if fps is unavailable
# fps = 30

# Define codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Use 'XVID' or 'MJPG' for .avi files
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (out_frame_width, out_frame_height))


# used to record the time when we processed last frame
prev_frame_time = 0
# used to record the time at which we processed current frame
new_frame_time = 0
count = 0
font = cv2.FONT_HERSHEY_SIMPLEX

# Calculate the center crop region
x_start = (frame_width - 720) // 2  # Horizontal start point
y_start = 0  # Vertical start point for 720 height

while cap.isOpened():
    # height, width, layers = image.shape
    # new_h = height / 2
    # new_w = width / 2
    # resize = cv2.resize(image, (new_w, new_h))
    # cv2.imwrite("%03d.jpg" % count, resize)
    # success, image = vidcap.read()
    # count += 1
    success, img = cap.read()

    if not success:
        break

    # count += 1

    # if count % 5 != 0:
    #     continue

    # Get the current frame size
    # height, width, _ = img.shape

    # Resize the frame
    # scale_percent = 20
    # new_width = int(width * scale_percent / 100)
    # new_height = int(height * scale_percent / 100)
    # dim = (new_width, new_height)
    # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    # results = []
    # process the resized image


    # # Capture frame-by-frame
    # ret, frame = cap.read()
    # if ret == True:

    #     # Read frame
    #     img = cv2.imread('Frame',frame)

    #     # Feed frame to model
    #     outs = net.forward(img)

    #     # plot your results...

    #     # Display frame
    #     # cv2.imshow('Frame',frame)

    #     # Press Q on keyboard to  exit
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break

    # # Break the loop
    # else:
    #     break

    # font = cv2.FONT_HERSHEY_SIMPLEX

    # is_detected = False
    # # coordinates
    # for r in results:
    #     boxes = r.boxes

    #     for box in boxes:
    #         # bounding box
    #         x1, y1, x2, y2 = box.xyxy[0]
    #         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

    #         # put box in cam
    #         cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

    #         # confidence
    #         confidence = math.ceil((box.conf[0]*100))/100
    #         # print("Confidence --->",confidence)

    #         # class name
    #         cls = int(box.cls[0])

    #         # print("Class name -->", classNames[cls])

    #         # object details
    #         org = [x1, y1]

    #         fontScale = 1
    #         color = (255, 0, 0)
    #         thickness = 2

    #         label = f'{classNames[cls]} - {confidence}'

    #         cv2.putText(img, label, org, font, fontScale, color, thickness)
    #         is_detected = True
    #         # else:
    #         #     # object details
    #         #     org = [x1, y1]
    #         #     font = cv2.FONT_HERSHEY_SIMPLEX
    #         #     fontScale = 1
    #         #     color = (0, 0, 255)
    #         #     thickness = 2

    #         #     cv2.putText(img, "unknown", org, font, fontScale, color, thickness)

    # Crop the center 720x720 region
    if crop_center_zone:
        cropped_frame = img[y_start:y_start + 720, x_start:x_start + 720]
        predictibile_frame = cv2.resize(cropped_frame, (out_frame_width, out_frame_height), interpolation = cv2.INTER_AREA)
    else:
        predictibile_frame = cropped_frame = cv2.resize(img, (out_frame_width, out_frame_height), interpolation = cv2.INTER_AREA)

    if model_id != 6:
        predictibile_frame = cv2.cvtColor(predictibile_frame, cv2.COLOR_RGB2BGR)

    result = predict_callable(predictibile_frame)

    out_frame = result['image']

    # st.markdown(f"Model: **{model.get_name()}**")
    # st.image(result['image'],caption=result['description'])


    new_frame_time = time.time()

    # Calculating the fps

    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    print(new_frame_time-prev_frame_time)
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    # converting the fps into integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)


    # putting the FPS count on the frame
    cv2.putText(out_frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    #frame = cv.flip(frame, 0)

    # write the flipped frame
    # Write the frame to the output video
    # w_img = cv2.resize(img, (640, 480), interpolation = cv2.INTER_AREA)

    # Write the cropped frame to the output video
    video_writer.write(out_frame)

    # Display the resized frame
    cv2.imshow('Resized Frame', out_frame)

    # # Wait for a key press
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break

    # if is_detected:
    #     cv2.waitKey(30000)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k != -1:
        cv2.waitKey()

# Release resources
cap.release()
video_writer.release()
cv2.destroyAllWindows()
