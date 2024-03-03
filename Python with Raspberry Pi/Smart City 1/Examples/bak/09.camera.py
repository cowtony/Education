#turns on and off a light emitting diode(LED) depending on motion sensor
import picamera
import RPi.GPIO as GPIO             #importing the RPi.GPIO module
import time                        #importing the time module
GPIO.cleanup()                     #to clean up at the end of your script
led_pin = 12                       #select the pin for the LED
motion_pin = 8                   #select the pin for the motion sensor
camera = picamera.PiCamera()

npic=0

def init():
  GPIO.setmode(GPIO.BOARD)         #to specify which pin numbering system
  GPIO.setwarnings(False)   
  GPIO.setup(led_pin,GPIO.OUT)                             #declare the led_pin as an output 
  GPIO.setup(motion_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #declare the motion_pin as an input
  print("-----------------------------------------------------------------------")  

init()

# Callback function to run when motion detected
def motionSensor(channel):
    global npic
    if GPIO.input(channel):     # True = Rising
        GPIO.output(led_pin, GPIO.HIGH)
        for i in range(1,5,1):
            camera.capture('image'+str(npic)+'.jpg')
            npic=npic+1
            time.sleep(0.5)
        print ("LED on")                           #print information
        time.sleep(5)        #delay 2s
        GPIO.output(led_pin, GPIO.LOW)
        print ("LED off")                           #print information

# add event listener on pin 21
GPIO.add_event_detect(motion_pin, GPIO.BOTH, callback=motionSensor, bouncetime=300) 

try:
    while True:
        time.sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print ("All cleaned up.")
