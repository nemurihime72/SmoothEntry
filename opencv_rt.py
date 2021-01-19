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
    img_path = args["image"]
    vid_path = args['video']
    if str(args["camera"]) == 'true':
        camera = True
    else:
        camera = False

    writer = None
    if args['output'] is not None and img_path is None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600))

    if camera:
        print('[INFO] Opening webcam')
        detectByCamera(writer)
    elif vid_path is not None:
        print('[INFO] Opening video from path')
        detectByPathVideo(vid_path, writer)
    elif img_path is not None:
        print('[INFO] opening image from path')
        detectByPathImage(img_path, args['output'])

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

def detectByPathVideo(path, writer):

    video = cv2.VideoCapture(path)
    check, frame = video.read()
    if check == False:
        print('Video not found. Please enter a valid path')
        return

    print('Detecting people...')
    while video.isOpened():
        check, frame = video.read()

        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()

def detectByPathImage(path, output_path):
    image = cv2.imread(path)
    image = imutils.resize(image, width = min(800, image.shape[1]))

    result = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to video file")
    arg_parse.add_argument("-i", "--image", default=None, help="path to image file")
    arg_parse.add_argument("-c", "--camera", default=False, help="Set True to use camera")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())

    return args

if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    humanDetector(args)
