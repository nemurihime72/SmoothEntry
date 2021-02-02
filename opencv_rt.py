# method 1

from __future__ import print_function
#from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import time
import cv2
import imutils
import numpy as np
import argparse
import nms
    
def detect(frame):
    bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride = (8, 8), padding = (8, 8), scale = 1.03)
    person = 0
    person1List = []
    person2List = []
    for x,y,w,h in bounding_box_coordinates:
        person += 1
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
        cv2.putText(frame, '{0} {1}'.format(x, y), (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 1)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1)
        #print(x, y)           
        if person == 1:
            person1List.append([x,y])
        elif person == 2:
            person2List.append([x,y])

    cv2.putText(frame, 'Press Q to quit', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,0,0) ,2)
    cv2.putText(frame, f'Total Persons: {person}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    #if person > 1:
    #    print('beep beep')    
    return frame, person1List, person2List

def humanDetector(args):
    writer = None
    if args['output'] is not None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600))

    print('[INFO] Opening webcam')
    detectByCamera(writer)

def detectByCamera(writer):
    vs = cv2.VideoCapture(0)
    #vs = PiVideoStream().start()
    time.sleep(2.0)
    fps = FPS().start()
    print('Detecting people...')
    
    while True:
        check, frame = vs.read()
        #frame = vs.read()
        #frame = imutils.resize(frame, width=400)
        frame = cv2.resize(frame, (640, 480))
        detector = detect(frame)
        frame = detector[0]
        p1List = detector[1]
        fps.update()
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            for i in p1List:
                print(i)
            break
    fps.stop()
    vs.release()
    cv2.destroyAllWindows()
    print("approx fps: {:.2f}".format(fps.fps()))


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())

    return args

if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    humanDetector(args)
    
    #camera = PiCamera()
    #camera.resolution = (640, 480)
    #camera.framerate = 32
    #rawCapture - PiRGBArray(camera, size = (640, 480))
    #stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

