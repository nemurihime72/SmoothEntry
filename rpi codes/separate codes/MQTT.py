#RPi
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
#config
LED_PIN = 24
BUTTON_PIN = 23
#init GPIO for LED and button
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#setup callback functions that are called when MQTT events hapen like connecting to the server
#or receiving data from a subscribed feed
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #subscribing in on connect() means that if we lose the connection and reconnect then subs will be renewed
    client.subscribe("/leds/pi")
#call back for when PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == '/leds/pi':
            if msg.payload == b'OFF':
                GPIO.output(LED_PIN, GPIO.HIGH)
            elif msg.payload == b'OFF':
                GPIO.output(LED_PIN, GPIO.LOW)
            elif msg.payload == b'TOGGLE':
                GPIO.output(LED_PIN, not GPIO.input (LED_PIN))\
#create mqtt client and connect to localhost
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)
print('Script is running, press ctrl-c to quit')
client.loop_start()
while True:
    #button_first = GPIO.input(BUTTON_PIN)
    input1 = input("1st input")
    time.sleep(0.02)
    #button_second = GPIO.input(BUTTON_PIN)
    input2 = input("2nd input")
    #if button_first == GPIO.HIGH and button_second == GPIO.LOW:
     #   print('button pressed')
      #  client.publish('/leds/esp8266', 'TOGGLE')
    if input1 == "a" and input2 == "b":
        print('button pressed')
        client.publish('/leds/esp8266', 'TOGGLE')