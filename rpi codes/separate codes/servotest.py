import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(23,GPIO.OUT)
servo1 = GPIO.PWM(23, 50)
GPIO.setup(12, GPIO.OUT)
servo2 = GPIO.PWM(12,50)

servo1.start(0)
servo2.start(0)
print("servo start")
time.sleep(1)

servo1.ChangeDutyCycle(8)
servo2.ChangeDutyCycle(8)
print("servo rotate")
time.sleep(30)

servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
print("servo stop")
servo1.stop()
servo2.stop()
GPIO.cleanup()
