import time                  #    time.sleep(seconds)
import RPi.GPIO as GPIO      # 0. Necessary for Raspberry Pi (GPIO)
from led4import import *     # 5. LCD, lcd_init()
import dht11                 # 6. Humidity & Temperature Sensor, dht11.DHT11(pin=TEMP_SENSOR)
from rc_time import rc_time  # 9. LDR: necessary to get brightness value

LED_PIN     = 10  # 1. lED pin: 10, 22
BUZZER_PIN  = 4   # 2. Buzzer pin: 4
BUTTON_PIN  = 9   # 3. Button pin: 9
BUTTON_PIN2 = 11  # 3. Button pin: 11
RELAY_PIN   = 27  # 4. Relay pin: 27
TEMP_SENSO  = 14  # 6. Humidity & temperature sensor pin: 14
MOTION_PIN  = 18  # 8. Motion Sensor pin: 18
LDR_PIN     = 12  # 9. Photoresistor (LDR) pin: 12

# Setup, initialization
def setup():
    GPIO.setmode(GPIO.BCM)            # 0. Raspberry Pi setup
    GPIO.setup(LED_PIN,    GPIO.OUT)  # 1. Output: LED
    GPIO.setup(BUZZER_PIN, GPIO.OUT)  # 2. Output: Buzzer
    GPIO.setup(RELAY_PIN,  GPIO.OUT)  # 4. Output: Repay
    lcd_init()                        # 5. Output: LCD
    # 3. Input: Button & button callback
    GPIO.setup(BUTTON_PIN,  GPIO.IN, pull_up_down=GPIO.PUD_UP)                               
    GPIO.add_event_detect(BUTTON_PIN,  GPIO.BOTH, callback=button_callback1, bouncetime=100)
    GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)                               
    GPIO.add_event_detect(BUTTON_PIN2, GPIO.BOTH, callback=button_callback2, bouncetime=100) 
    # 8. Input: Motion & motion callback
    GPIO.setup(MOTION_PIN,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                          
    GPIO.add_event_detect(MOTION_PIN, GPIO.RISING, callback=motionCallback, bouncetime=200) 

def button_callback1(channel): # 3. Execute this function when button pressed
    print('Button 1 pressed')

def button_callback2(channel): # 3. Execute this function when button2 pressed
    print('Button 2 pressed')

def motionCallback(channel):   # 8. Execute this function when motion detected
    print('Motion Detected')

# main function
def main():
    GPIO.output(LED_PIN,    True)                   # 1. LED: True for On, False for Off
    GPIO.output(BUZZER_PIN, False)                  # 2. Buzzer: True for On, False for Off
    GPIO.output(RELAY_PIN,  True)                   # 4. Relay: True for On, False for Off
    lcd_string("string here", LCD_LINE_1)           # 5. LCD: LCD_LINE_1 or LCD_LINE_2
    sensor_instance = dht11.DHT11(pin=TEMP_SENSOR)  # 6. Temperature: initialization
    while True:
        buttonStatus = GPIO.input(BUTTON_PIN) # 3. Button: 0 is pressed, 1 is not.
        motionStatus = GPIO.input(MOTION_PIN) # 8. Motion: Return True if motion detected
        result       = sensor_instance.read() # 6. result.temperature & result.humidity
        brightness   = rc_time(LDR_PIN)       # 9. LDR: Lower value for higher brightness
        time.sleep(0.01)

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        lcd_byte(0x01, LCD_CMD) # 5. LCD clean up
        GPIO.()          # 0. Finishing, clean up memory
