# Function:
# Button 1 - GPIO 11
# Button 2 - GPIO 9
# Buzzer   - GPIO 4
# LED      - GPIO 10

# Press button 1 to start the alarm and LED
# Press button 2 to stop  the alarm and LED

import RPi.GPIO as GPIO
import time

BUTTON_PIN  = 11
BUTTON_PIN2 = 9
LED_PIN     = 10
BUZZER_PIN  = 4
ON = True
OFF = False

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH, callback=button_callback,   bouncetime=100)
    GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN2, GPIO.BOTH, callback=button_callback2, bouncetime=100)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN,    GPIO.OUT)

def main():
    while True:
        print("I'm working...")
        time.sleep(1)
        

#button1 callback function for turn on buzzer and LED
def button_callback(channel):
    print("button pressed!")

    if(GPIO.input(BUTTON_PIN) == 0):
        print ("Button is pressed!")
        print ("Buzzer will be turn on!")
        GPIO.output(BUZZER_PIN, ON)
        GPIO.output(LED_PIN,    ON)    
    
    
#button2 callback function for turn off buzzer and LED
def button_callback2(channel):
    print("button2 pressed!")

    if(GPIO.input(BUTTON_PIN2) == 0):
        print ("Button2 is pressed!")
        print ("Buzzer will be turn OFF!")
        GPIO.output(BUZZER_PIN, OFF)
        GPIO.output(LED_PIN,    OFF)    
            

if __name__  == '__main__':
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()
