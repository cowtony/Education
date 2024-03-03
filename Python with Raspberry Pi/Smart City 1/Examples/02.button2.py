# Function
# Press button to turn on the buzzer and LED
# Button - GPIO 11
# LED    - GPIO 10
# Buzzer - GPIO 4


import RPi.GPIO as GPIO
import time

BUTTON_PIN = 11
LED_PIN    = 10
BUZZER_PIN = 4
ON = True
OFF = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH, callback=button_callback, bouncetime=200)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN,    GPIO.OUT)

def main():
    while True:
        print("I'm working...")
        time.sleep(1)
        

def button_callback(channel):
    print("button pressed!")

    if(GPIO.input(BUZZER_PIN) == 0):
        print ("Button is pressed!")
        print ("Buzzer will be turn on!")
        GPIO.output(BUZZER_PIN, ON)
        GPIO.output(LED_PIN,    ON)
    else:
        GPIO.output(BUZZER_PIN, OFF)
        GPIO.output(LED_PIN,    OFF)
        print ("Buzzer is OFF!")

if __name__  == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
