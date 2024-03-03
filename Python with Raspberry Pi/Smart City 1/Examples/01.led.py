import RPi.GPIO as GPIO
import time

LED_PIN = 10
ON = True
OFF = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def main():
    while True:
        GPIO.output(LED_PIN, ON)
        time.sleep(1)
        GPIO.output(LED_PIN, OFF)
        time.sleep(1)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
