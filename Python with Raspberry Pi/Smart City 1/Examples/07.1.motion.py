import RPi.GPIO as GPIO
import time

LED_PIN = 10
MOTION_PIN = 18

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED_PIN,GPIO.OUT)
  GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.add_event_detect(MOTION_PIN, GPIO.RISING, callback=motionCallback, bouncetime=200)

def main():
    while True:
        time.sleep(0.01)
        if GPIO.input(MOTION_PIN):
            print("Motion detected")
        else:
            print('No motion detected')

def motionCallback(channel):
    if GPIO.input(channel):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
