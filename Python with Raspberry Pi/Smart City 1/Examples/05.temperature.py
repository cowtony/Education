import smbus
import time
import dht11
import RPi.GPIO as GPIO
from led4import import *

TEMP_SENSOR = 14

def setup():
    GPIO.setmode(GPIO.BCM)
    lcd_init()

def main():
    sensor_instance = dht11.DHT11(pin = TEMP_SENSOR)
    while True:
        result = sensor_instance.read()
        if result.is_valid():
    	    lcd_string("Temperature: " + str(result.temperature) + "C", LCD_LINE_1)
    	    lcd_string("Humidity: " + str(result.humidity) + "%", LCD_LINE_2)
    	    time.sleep(3)
    	    lcd_string("Innovaker", LCD_LINE_1)
    	    lcd_string("Tutorial", LCD_LINE_2)
    	    time.sleep(3)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        lcd_byte(0x01, LCD_CMD)
        GPIO.cleanup()
