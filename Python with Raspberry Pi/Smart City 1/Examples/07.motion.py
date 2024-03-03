import RPi.GPIO as GPIO
import time

LED_PIN = 10
MOTION_PIN = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    while True:
        value = GPIO.input(MOTION_PIN)
        if value:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(15)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
