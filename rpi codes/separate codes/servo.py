from time import sleep
import time
import wiringpi

#use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

#set #18 to be pwm output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

#set the pwm mode to milliseconds style
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

#divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.1

print("press a to move up, b to move down and c to stop")

while True:
    key = input()
    if key == 'a':
        # move up
        wiringpi.pwmWrite(18, 200)
    elif key == 'b':
        # move down
        wiringpi.pwmWrite(18, 100)
    elif key == 'c':
        # stop
        wiringpi.pwmWrite(18, 0)
    elif key == 'e':
        # exit
        exit()
