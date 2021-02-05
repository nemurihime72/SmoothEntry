import RPi.GPIO as GPIO
import time
from time import sleep

#dismisses error messages
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#create a blinking method
def blinking(pin):
    #turns on LED for 2 seconds
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(2)
    #turns off LED for 2 seconds
    GPIO.output(pin,GPIO.LOW)
    time.sleep(2)
    return

#states where LED pin is
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

#calling the blinking method over a span of 20s
for i in range(0, 40):
    blinking(LED_PIN)

GPIO.cleanup()
