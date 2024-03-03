import RPi.GPIO as GPIO
from neopixel import *
import time

BUTTON1_PIN    = 11
BUTTON2_PIN    = 9

# LED strip configuration:
LED_COUNT      = 2       # Number of LED pixels.
LED_PIN        = 13      # GPIO pin connected to the pixels (12, 18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 050     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON1_PIN, GPIO.BOTH, callback=changeColor, bouncetime=200)
    GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON2_PIN, GPIO.BOTH, callback=WLED_On_Off, bouncetime=200)
    
    global strip
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    global WLED_STATUS
    WLED_STATUS = False
    global color
    color = 1

def wheel(pos):
    if pos < 85:
	return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
	pos -= 85
	return Color(255 - pos * 3, 0, pos * 3)
    else:
	pos -= 170
	return Color(0, pos * 3, 255 - pos * 3)

def changeColor(channel):
    global color
    color = (color + 85) % 255
    
def WLED_On_Off(channel):
    global WLED_STATUS
    WLED_STATUS = not WLED_STATUS
    
def setWLEDcolor(color):
    global strip
    for index in range(LED_COUNT):
        strip.setPixelColor(index, color)
    strip.show()
    
def main():
    global strip
    strip.begin()
    print ('Press Ctrl-C to quit.')
    while True:
        global WLED_STATUS
        if WLED_STATUS == True:
            global color
            setWLEDcolor(wheel(color & 255))
            color += 1
        else:
            setWLEDcolor(0)
            
        time.sleep(0.05)
        
    
if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        setWLEDcolor(0)
        GPIO.cleanup()
