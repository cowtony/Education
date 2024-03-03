import RPi.GPIO as GPIO
import time

#PIN NUMBERS
LED_PINS = [10, 22, 25, 8, 7, 16, 20, 21]

#ON OFF CONSTANTS
ON = 1
OFF = 0

def setup():
    GPIO.setmode(GPIO.BCM)

    for i in range(len(LED_PINS)):
        GPIO.setup(LED_PINS[i], GPIO.OUT)
        GPIO.output(LED_PINS[i], OFF)

def run():
    index = 0
    while True:
        GPIO.output(LED_PINS[index], OFF)
        index = (index + 1) % 7
        GPIO.output(LED_PINS[index], ON)
        time.sleep(0.5)

setup()
run()
