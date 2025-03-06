import cv2
import numpy as np
import random
import os
import common

panneau_shape = (64, 64)
rep_non_panneaux = "non_panneaux"

video = "video\video01.mp4"

cap = cv2.VideoCapture(video)

no_image = 0
nombre_images = 100000

nombre_images_par_frame = int(nombre_images / cap.get(cv2.CAP_PROP_FRAME_COUNT)) + 1

while True:
    resp, frame = cap.read()
    if resp is False:
        quit()
    h, w, c = frame.shape

    for cpt in range(nombre_image_par_frame):
        x = random.randint(0, w - panneau_shape[1])
        y = random.randint(0, h - panneau_shape[0])
        image = frame[y:y + panneau_shape[0], x:x + panneau_shape[1]]        
        cv2.imwrite(rep_non_panneaux + "\{:d}.png".format(no_image), image)
        no_image += 1
        if no_image == nombre_images :
            quit()
    


        
