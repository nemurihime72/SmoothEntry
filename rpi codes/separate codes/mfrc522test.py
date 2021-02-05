import time
import RPi.GPIO as GPIO
import mfrc522 as MFRC522

MIFAREReader = MFRC522.MFRC522()

print("looking for cards")
print("press ctrl c to stop")

try:
    while True:
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        if status == MIFAREReader.MI_OK:
            print("UID: "+str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))

            time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
