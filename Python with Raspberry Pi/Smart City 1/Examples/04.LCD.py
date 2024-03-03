import RPi.GPIO as GPIO
import time
from led4import import *
from datetime import datetime

def setup():
    lcd_init()

def main():
	while True:
		lcd_string(str(datetime.now()), LCD_LINE_1)
		lcd_string("Innovaker 2018", LCD_LINE_2)
		time.sleep(60)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        lcd_byte(0x01, LCD_CMD)
        GPIO.cleanup()
