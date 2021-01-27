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
        print(x, y)

    cv2.putText(frame, 'Press Q to quit', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,0,0) ,2)
    cv2.putText(frame, f'Total Persons: {person}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    #if person > 1:
        #print('beep beep')

    return frame

def humanDetector(args):
    writer = None
    if args['output'] is not None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600))

    print('[INFO] Opening webcam')
    detectByCamera(writer)

def detectByCamera(writer):
    video = cv2.VideoCapture(0)
    print('Detecting people...')
    
    while True:
        check, frame = video.read()
        frame = cv2.resize(frame, (640, 480))
        frame = detect(frame)

        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


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
