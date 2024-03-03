import picamera
from time import sleep


camera = picamera.PiCamera()

def keep():
    camera.start_preview()
    camera.start_recording('video.h264')
    sleep(5)
    camera.stop_recording()
    camera.capture('image1.jpg')
    camera.start_preview()
    sleep(15)
    camera.stop_preview()

camera.capture('image1.jpg')








    
    