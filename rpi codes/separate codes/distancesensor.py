import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BCM)

    #pins to use
    PIN_TRIG = 20
    PIN_ECHO = 16

    #set as output and input
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIG, False)

    time.sleep(0.5)

    GPIO.output(PIN_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIG, False)
    start = time.time()

    while GPIO.input(PIN_ECHO) == 0:
        start = time.time()

    while GPIO.input(PIN_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 34300
    distance = distance / 2
    if distance <= 40:
        print("person detected")
        print("Distance: {0:.2f}".format(distance))
