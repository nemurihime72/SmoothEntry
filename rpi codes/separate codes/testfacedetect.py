from picamera.array import PiRGBArray
from picamera import PiCamera
from imutils.video.pivideostream import PiVideoStream
import time
import cv2

def detect_face():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #cap = cv2.VideoCapture(0)
    cap = PiVideoStream().start()
    time.sleep(2.0)
    face_detected = False
    while (True):
        # Read the frame
        #_, img = cap.read()
        frame = cap.read()
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
    cap.release()
    cv2.destroyAllWindows()
    if face_detected == True:
            return True
    return False


while True:
    if detect_face() == True:
        print("success")
    else:
        print("failure")
