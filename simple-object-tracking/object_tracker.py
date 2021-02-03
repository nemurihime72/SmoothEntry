# method 3

# from pyimagesearch, modified for use for assignment

# USAGE
# python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from pyimagesearch.centroidtracker import CentroidTracker
from imutils.video import VideoStream
from imutils.video import FPS
from threading import Thread
from playsound import playsound
import nms
#from imutils.object_detection import non_max_suppression	
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt",
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model",
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize our centroid tracker and frame dimensions
ct = CentroidTracker()
(H, W) = (None, None)

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

checkIn = False

personLeft = 0
personRight = 0

# load our serialized model from disk
#print("[INFO] loading model...")w
#net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# read the next frame from the video stream and resize it
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	#print(checkIn)
		

	# if the frame dimensions are None, grab them
	if W is None or H is None:
		(H, W) = frame.shape[:2]
	
	cv2.line(frame, (150, 0), (150, H), (0, 255, 255), 2)

	bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride = (6, 6), padding = (8, 8), scale = 1.05)
	rects = []
	person = 0
	for x,y,w,h in bounding_box_coordinates:
		person += 1
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
		cv2.putText(frame, '{0} {1}'.format(x, y), (x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 1)
		cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1)
		rects.append([x, y, x+w, y+h])

	
	# update our centroid tracker using the computed set of bounding
	# box rectangles
	objects = ct.update(rects)
	personLeft = 0
	personRight = 0	

	# loop over the tracked objects
	for (objectID, centroid) in objects.items():	
		if centroid[0] < 150:	
			personLeft += 1
		# draw both the ID of the object and the centroid of the
		# object on the output frame
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.putText(frame, f'person left {personLeft}', (10, H-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
		
		if checkIn == False and personLeft > 0:	
			print("beep")
			#playsound('C:\\Users\\Ryan\\Documents\\SmoothEntry\\simple-object-tracking\\sounds\\beep.mp3')
		elif checkIn == True and personLeft == 1:	
			print("customer entered store")
			time.sleep(1)
			checkIn = False
		elif checkIn == True and personLeft > 1:	
			print("beep beep")
			#playsound('C:\\Users\\Ryan\\Documents\\SmoothEntry\\simple-object-tracking\\sounds\\beep.mp3')



	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	elif key == ord("w"):	
		checkIn = True
		print(checkIn)

	elif key == ord("e"):	
		checkIn = False
		print(checkIn)
		
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

