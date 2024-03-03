import RPi.GPIO as GPIO
import time

BUTTON_PIN = 11
BUZZER_PIN = 4
ON = True
OFF = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def main():
    while True:
        time.sleep(0.01)
        if(GPIO.input(BUTTON_PIN) == 0):
            print ("Button is pressed!")
            print ("Buzzer will be turn on!")
            GPIO.output(BUZZER_PIN, ON)
        else:
            GPIO.output(BUZZER_PIN, OFF)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
