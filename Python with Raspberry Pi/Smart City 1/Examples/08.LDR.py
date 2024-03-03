import RPi.GPIO as GPIO
import time

LED_PIN = 10
LDR_PIN = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def rc_time(pin):
    count = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)

    while(GPIO.input(pin) == GPIO.LOW):
        count += 1

    return count

def main():
    while True:
        brightness = rc_time(LDR_PIN)
        print(brightness)
        if brightness > 600:
          GPIO.output(LED_PIN, GPIO.HIGH)
          time.sleep(1)
        else:
          GPIO.output(LED_PIN, GPIO.LOW)
          time.sleep(1)


if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
