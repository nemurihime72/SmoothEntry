import RPi.GPIO as GPIO
import time
import socket
import sys

def link_tag()
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
    
def fake_link_tag:
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
            if firebase.get("/users", 'A52121D241') == None:
                nric = input("Please enter user's NRIC: ")
                name = input("Please enter user's name: ")
                phonenumber = input("Please enter user's phone number: ")
                firebase.put("/users/", '{0}'.format(data), {"NRIC":nric, "name":name, "phonenumber":phonenumber, "checked_in1":"false","checked_in2":"false", "current_temp":"none", "height":"test"})
                print("The user has been successfully linked to the RFID tag!")
                break
            else:
                print("This RFID tag is already in use!")
                break

#link_tag()
#fake_link_tag()
