import RPi.GPIO as GPIO
import time

RELAY_PIN = 27
ON = True
OFF = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

def main():
    while True:
        GPIO.output(RELAY_PIN, ON)
        time.sleep(2)
        GPIO.output(RELAY_PIN, OFF)
        time.sleep(2)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
