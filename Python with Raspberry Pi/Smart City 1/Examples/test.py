import RPi.GPIO as GPIO
import time
import dht11
from led4import import *
import smbus
import RPi.GPIO as GPIO
from led4import import *


ON = 1
OFF = 0

led=[4,27,17,10,22,25,8,7,16,20,21]
Button_pin1 = 9
Button_pin2 = 11
Buzzer_pin = 4
motion_pin = 18
Temp_sensor=14
LDR_pin_to_circuit = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(Button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motion_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #declare the motion_pin as an input

for i in range(len(led)):
    GPIO.setup(led[i], GPIO.OUT)
    GPIO.output(led[i],False)

def leds(status):
    led1=[27,17,10,22,25,8,7,16,20,21]
    for i in range(len(led1)):
        GPIO.output(led1[i], status)


def my_callback(channel):
    print("button pressed!")

    BuzzerStatus = GPIO.input(Buzzer_pin)
    if BuzzerStatus:
        GPIO.output(Buzzer_pin, GPIO.LOW)
        pass
    else:
        GPIO.output(Buzzer_pin, GPIO.HIGH)
        pass
    pass


GPIO.add_event_detect(Button_pin1, GPIO.FALLING, callback=my_callback,bouncetime=200)
GPIO.add_event_detect(Button_pin2, GPIO.FALLING, callback=my_callback,bouncetime=200)


# Callback function to run when motion detected
def motionSensor(channel):
    if GPIO.input(channel):     # True = Rising
##        GPIO.output(Buzzer_pin, GPIO.HIGH)
        leds(1)
        print ("Motion LED on")                           #print information
        time.sleep(2)        #delay 2s
##        GPIO.output(Buzzer_pin, GPIO.LOW)
        leds(0)
        print ("Motion LED off")                           #print information

GPIO.add_event_detect(motion_pin, GPIO.BOTH, callback=motionSensor, bouncetime=300)

#----- LDR testing
def rc_time (LDR_pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(LDR_pin_to_circuit, GPIO.OUT)
    GPIO.output(LDR_pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(LDR_pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(LDR_pin_to_circuit) == GPIO.LOW):
        count += 1

    return count



def th():
    lcd_init()
    instance = dht11.DHT11(pin = Temp_sensor)

    result = instance.read()
    # Send some test

    if result.is_valid():
	    lcd_string("temp:"+str(result.temperature)+" C",LCD_LINE_1)
	    lcd_string("humid:"+str(result.humidity)+"%"+"LDR:"+str(rc_time(LDR_pin_to_circuit)),LCD_LINE_2)
	    time.sleep(3)
#----------------- end of def th() ---------



leds(ON)
GPIO.output(Buzzer_pin, GPIO.HIGH)
time.sleep(3)
GPIO.output(Buzzer_pin, GPIO.LOW)
leds(OFF)
# loop through 50 times, on/off for 1 second
while True:
    th()
    time.sleep(1)

GPIO.cleanup()
