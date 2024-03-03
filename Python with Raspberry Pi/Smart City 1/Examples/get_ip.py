import RPi.GPIO as GPIO
import time
import socket
from led4import import *
from datetime import datetime

Buzzer_PIN = 4

def setup():
    lcd_init()
    time.sleep(15)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer_PIN, GPIO.OUT)

def get_ip_address():
     ip_address = '';
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.connect(("8.8.8.8",80))
     ip_address = s.getsockname()[0]
     s.close()
     return ip_address

def main():
        GPIO.output(Buzzer_PIN, True)
        time.sleep(1)
        GPIO.output(Buzzer_PIN, False)        

        lcd_string("Local IP Address:", LCD_LINE_1)
        lcd_string(get_ip_address(), LCD_LINE_2)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
#        lcd_byte(0x01, LCD_CMD)
        GPIO.cleanup()
