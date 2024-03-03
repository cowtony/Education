import RPi.GPIO as GPIO
import time

LED_PIN = 10
BUZZER_PIN=4
LDR_PIN = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def rc_time (pin):
    count = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)

    while(GPIO.input(LDR_PIN) == GPIO.LOW):
        count += 1

    return count

def main():
  while True:
    brightness = rc_time(LDR_PIN)
    print (brightness)

    if brightness > 10:
        GPIO.output(LED_PIN,GPIO.HIGH)
        GPIO.output(BUZZER_PIN,GPIO.HIGH)
    else:
        GPIO.output(LED_PIN,GPIO.LOW)
        GPIO.output(BUZZER_PIN,GPIO.LOW)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
