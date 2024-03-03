#!/usr/bin/env python3
# Research picamera package
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import apriltag

# initialize the camera and grab a reference to the raw camera capture
#Set kwidth & kheight


#Call PiCamera() assign result to variable "camera"

#Use camer.resolution to resolution = (kwidth, kheight)

#Use camera.frame to set framerate = 20

#Call PiRGBArray(), assign to variable "rawCapture"


# allow the camera to warmup
#use Sleep() for 0.1s

#Print "cam ready"


# capture frames from the camera
#Loop to get camera_frame, using camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

    #use cameraframe.array assign to variable "frame"
    
    #Display image in window using cv2.imshow()
    

    #Terminate code - no need to write by yourself
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    rawCapture.truncate(0)
cv2.destroyAllWindows()