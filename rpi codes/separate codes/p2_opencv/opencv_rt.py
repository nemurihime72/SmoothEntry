from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils
import numpy as np
import argparse
import nms
    
def detect(frame):
    bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride = (8, 8), padding = (8, 8), scale = 1.03)
    person = 0
    for x,y,w,h in bounding_box_coordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1

    cv2.putText(frame, 'Press Q to quit', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,0,0) ,2)
    cv2.putText(frame, f'Total Persons: {person}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    if person > 1:
        print('beep beep')
    return frame

def humanDetector(args):
    if str(args["camera"]) == 'true':
        camera = True
    else:
        camera = False
    writer = None
    if camera:
        print('[INFO] Opening webcam')
        detectByCamera(writer)

def detectByCamera(writer):
    #video = cv2.VideoCapture(0)
    vs = PiVideoStream().start()
    time.sleep(2.0)
    fps = FPS().start()
    print('Detecting people...')
    
    while True:
        #check, frame = video.read()
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        #frame = cv2.resize(frame, (640, 480))
        frame = detect(frame)
        fps.update()
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    fps.stop()
    #vs.release()
    cv2.destroyAllWindows()
    print("approx fps: {:.2f}".format(fps.fps()))


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-c", "--camera", default=False, help="Set True to use camera")
    args = vars(arg_parse.parse_args())

    return args

if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    humanDetector(args)
    
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture - PiRGBArray(camera, size = (640, 480))
    stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

