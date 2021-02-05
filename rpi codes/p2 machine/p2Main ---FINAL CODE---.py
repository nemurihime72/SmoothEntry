# General libaries
import time
from time import sleep
import math
import cv2
import sys
import socket

#For Firebase
from firebase.firebase import FirebaseApplication
from datetime import datetime

# For LCD Module
import lcddriver

# For LED, Motor and Distance Sensor Modules
import RPi.GPIO as GPIO

# For Motor Module
import wiringpi

# For Camera Module
from picamera.array import PiRGBArray
from picamera import PiCamera
import imutils
from imutils.video.pivideostream import PiVideoStream

# For Thermal Camera Module
import os
import busio
import board
import numpy as np
import pygame
from scipy.interpolate import griddata
from colour import Color
import adafruit_amg88xx


url = "https://smoothentry-74b63-default-rtdb.firebaseio.com/"
firebase = FirebaseApplication(url, None)

display = lcddriver.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def link_tag1():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        while True:
        
            GPIO.setmode(GPIO.BCM)

            #pins to use
            PIN_TRIG = 20
            PIN_ECHO = 16

            #set as output and input
            GPIO.setup(PIN_TRIG, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            #set trigger to false
            GPIO.output(PIN_TRIG, False)

            #allow module to settle
            time.sleep(0.5)

            #send a 10us pulse to trigger
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
            if distance < 6:
                
                message = b'A52121D241'
                print('sending {!r}'.format(message))
                sock.sendall(message)
                break
                
    ##    # Look for the response
    ##    amount_received = 0
    ##    amount_expected = len(message)
    ##
    ##    while amount_received < amount_expected:
    ##        data = sock.recv(16)
    ##        amount_received += len(data)
    ##        print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()
    
def link_tag2():
    while True:
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #pins to use
        PIN_TRIG = 20
        PIN_ECHO = 16

        #set as output and input
        GPIO.setup(PIN_TRIG, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        #set trigger to false
        GPIO.output(PIN_TRIG, False)

        #allow module to settle
        time.sleep(0.5)

        #send a 10us pulse to trigger
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
        UID = "A52121D241"
        if distance < 6:
            if firebase.get("/users", UID) == None:
                nric = input("Please enter user's NRIC: ")
                name = input("Please enter user's name: ")
                phonenumber = input("Please enter user's phone number: ")
                firebase.put("/users/", UID, {"nric":nric, "name":name, "phone_number":phonenumber, "checked_in":"false", "latest_temp":"none", "height":"none"})
                print("The user has been successfully linked to the RFID tag, {}.".format(UID))
                break
            else:
                print("This RFID tag is already in use!")
                break

#Claris/Keith
def person_present():
    while True:
        GPIO.setmode(GPIO.BCM)

        #pins to use
        PIN_TRIG = 20
        PIN_ECHO = 16

        #set as output and input
        GPIO.setup(PIN_TRIG, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        #set trigger to false
        GPIO.output(PIN_TRIG, False)

        #allow module to settle
        time.sleep(0.5)

        #send a 10us pulse to trigger
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
        if distance <= 15:
#            print(distance)
            return True
    return False



#Linus
def detect_face():
    #camera = PiCamera()
    #camera.resolution = (640, 480)
    #camera.framerate = 32
    #rawCapture = PiRGBArray(camera, size = (640, 480))
    #stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #cap = cv2.VideoCapture(0)
    cap = PiVideoStream().start()
    time.sleep(2.0)
    face_detected = False
    while face_detected == False:
        # Read the frame
        #_, img = cap.read()
#        print('looking for faces')
        frame = cap.read()
        frame = imutils.resize(frame, width=400)
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)
#            print("face detected")
            face_detected = True

    # When everything done, release the capture
    cap.stop()
    cv2.destroyAllWindows()
    if face_detected == True:
            return True
    return False

#Linus

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map_value(x, in_min, in_max, out_min, out_max):

    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


#Linus
def diplay_thermal_camera_view():
    i2c_bus = busio.I2C(board.SCL, board.SDA)

    MINTEMP = 20

    MAXTEMP = 30

    COLORDEPTH = 1024

    os.putenv('SDL_FBDEV', '/dev/fb1')

    pygame.init()

    sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

    points = [(math.floor(ix/8), (ix%8)) for ix in range (0,64)]
    grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

    height = 240
    width =240

    blue = Color("indigo")
    colors = list(blue.range_to(Color("red"), COLORDEPTH))

    colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

    displayPixelWidth = width / 30
    displayPixelHeight = height / 30

    lcd = pygame.display.set_mode((width, height))

    lcd.fill((255,0,0))

    pygame.display.update()
    pygame.mouse.set_visible(False)

    lcd.fill((0, 0 ,0))

    pygame.display.update()

    while True:
        pixels = []
        for row in sensor.pixels:
            pixels = pixels + row
        pixels = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]

        bicubic = griddata(points, pixels, (grid_x, grid_y), method = 'cubic')

        for ix, row in enumerate(bicubic):
            for jx, pixels in enumerate(row):
                pygame.draw.rect(lcd, colors[constrain(int(pixels), 0, COLORDEPTH - 1)],
                                 (displayPixelHeight * ix, displayPixelWidth * jx,
                                  displayPixelHeight, displayPixelWidth))
        pygame.display.update()
    

#Linus
def get_temperature():
    i2c_bus = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus)
    temperature = sensor.pixels[4][2] + 8
    if temperature < 37.5:
        try:
            firebase.patch("/users/" + "A52121D241", {"latest_temp": sensor.pixels[4][2] + 8})
            return True
        except:
            print("Could not update the users temperature!")
            return False
    else:
        return "sick"

    
    
#Linus
def check_in():
    while True:
      
        GPIO.setmode(GPIO.BCM)

        #pins to use
        PIN_TRIG = 20
        PIN_ECHO = 16

        #set as output and input
        GPIO.setup(PIN_TRIG, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        #set trigger to false
        GPIO.output(PIN_TRIG, False)

        #allow module to settle
        time.sleep(0.5)

        #send a 10us pulse to trigger
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
        UID = "A52121D241"
        storeno = "20"
        currentdate = datetime.today().strftime("%d-%m-%Y")
        if distance < 5:
            try:
                print(distance)
                # To check if RFID is registered in the database
                if firebase.get("/users/" + UID, "checked_in") == "false":
                    firebase.put("/users/" + UID, "checked_in", "true")
                    if firebase.get("/stores/" + storeno, currentdate) == None:
                        firebase.put("/stores/" + storeno, currentdate, 0)
                        print("please")
                    else:
                        newtotal = int(firebase.get("/stores/" + storeno, currentdate))
                        newtotal += 1
                        firebase.patch("/stores/" + storeno, {currentdate: newtotal})
                        print("work")                
                    print("success")
                    return True
            except:
                print("Not able to check in!")
                return False

#         if time.time() - start > 10:
#             break
                
#Linus
def display_success_lcd():
    print("Writing to display")
    display.display_string("Successful!", 1)
    display.display_string("Temp: " + "{0:.2f}".format(float(firebase.get("/users/A52121D241/", "latest_temp"))),2)
    time.sleep(2)

    display.clear()

def display_sick_lcd():
    print("Writing to display")
    display.display_string("You sick!", 1)
    display.display_string("Go home!", 2)

def display_failure_lcd():
    print("Writing to display")
    display.display_string("Check-in", 1)
    display.display_string("unsuccessful!", 2)
    time.sleep(2)

    display.clear()

def blinking(pin):
    #turns on LED for 0.1 seconds
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    #turns off LED for 0.1 seconds
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    return
   
#Linus
def show_success_led():
   #states where the LED pin is
   GREEN_LED_PIN1 = 12
   GREEN_LED_PIN2 = 13
   GPIO.setup(GREEN_LED_PIN1, GPIO.OUT)
   GPIO.setup(GREEN_LED_PIN2, GPIO.OUT)

   #Calling the Blinking method over a span of 6 seconds
   for i in range (0, 2):
      blinking(LED_PIN)

   GPIO.cleanup()

def show_failure_led():
      #states where the LED pin is
   RED_LED_PIN1 = 12
   RED_LED_PIN2 = 13
   GPIO.setup(RED_LED_PIN1, GPIO.OUT)
   GPIO.setup(RED_LED_PIN2, GPIO.OUT)

   #Calling the Blinking method over a span of 6 seconds
   for i in range (0, 2):
      blinking(LED_PIN)

   GPIO.cleanup()
   
#Linus
def check_out():
    UID = "A52121D241"

    while True:
        
        GPIO.setmode(GPIO.BCM)

        #pins to use
        PIN_TRIG = 20
        PIN_ECHO = 16

        #set as output and input
        GPIO.setup(PIN_TRIG, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        #set trigger to false
        GPIO.output(PIN_TRIG, False)

        #allow module to settle
        time.sleep(0.5)

        #send a 10us pulse to trigger
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
        if distance < 6:
            try:
                if firebase.get("/users/" + UID, "checked_in") == "true":
                    firebase.put("/users/" + UID, "checked_in", "false")
                return True
            except:
                return False


    
##    while continue_reading:
##    
##        # Scan for cards    
##        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
##        
##        # Get the UID of the card
##        (status,uid) = MIFAREReader.MFRC522_Anticoll()
##        uid_value = to_int(uid)
##        UID = hex(uid_value)
##        
##        # If we have the UID, continue
##        if status == MIFAREReader.MI_OK:
##            # To check if RFID is registered in the database
##            if firebase.get("/users/" + UID, "checked_in") == "true":
##                firebase.put("/users/", UID, {"checked_in":"false"}
##                return True
##            else:
##                return False

def servo(direction):
    
    while True:
        #key = input()
        if direction == 'up':
            # move up
            print('up')
            wiringpi.pwmWrite(18, 200)
        elif direction == 'down':
            # move down
            print('down')
            wiringpi.pwmWrite(18, 100)
            if detect_face() == True:
                direction = 'stop'
        elif direction == 'stop':
            # stop
            print('stop')
            wiringpi.pwmWrite(18, 0)
            break


def menu():
    menu_list = ["Run SmoothEntry", "Link RFID Tag", "Display Thermal Camera", "Check out", "Exit"]
    i = 0
    print("-------- SmoothEntry --------\n")
    for i in range(len(menu_list)):
        if menu_list[i] == "Exit":
            print("[0] {0}".format(menu_list[i]))
        else:
            print("[{0}] {1}".format((i+1),menu_list[i]))
    print("\n-----------------------------")
        

def smoothentry():
    if __name__ == "__main__":

        #print('test')
        
        #use 'GPIO naming'
        wiringpi.wiringPiSetupGpio()
        #print('test')

        #set #18 to be pwm output
        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
        #print('test')

        #set the pwm mode to milliseconds style
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        #print('test1')

        #divide down clock
        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(2000)

        delay_period = 0.1
        #print('test')
        personPresent = person_present()
        if personPresent == True:
            servo('down')
            success = check_in()
            temp = get_temperature()
            if success == True and temp == True:
                display_success_lcd()
            elif temp == "sick":
                display_sick_lcd()
            else:
                display_failure_lcd()

option = -1
while option != 0:
    menu()
    option = input("Please enter option:")
    if option == "1":
        smoothentry()
    elif option == "2":
        #link_tag1()
        link_tag2()
    elif option == "3":
        diplay_thermal_camera_view()
    elif option == "4":
        check_out()
    elif option == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")

