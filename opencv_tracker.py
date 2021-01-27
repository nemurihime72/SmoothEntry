from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import nms

#contruct arg parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, help="path to video file")
ap.add_argument("-t", "--tracker", type=str, default="csrt", help="opencv obj tracker type")
args = vars(ap.parse_args())

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#extract the opencv ver info
(major, minor) = cv2.__version__.split(".")[:2]

#if opencv ver <=3.2, use special factory function to create object tracker
if (int(major) == 3 and int(minor) < 3):
    tracker = cv2.Tracker_create(args["tracker"].upper())

#else, need to explicitly call appropriate object tracker constructor
#else:
    #initialise a dict that maps string to their corresponding opencv obj tracker implementation
    #OPENCV_OBJECT_TRACKERS = {
        #"csrt": cv2.TrackerCSRT_create,
        #"kcf": cv2.TrackerKCF_create,
		#"boosting": cv2.TrackerBoosting_create,
		#"mil": cv2.TrackerMIL_create
		#"tld": cv2.TrackerTLD_create,
		#"medianflow": cv2.TrackerMedianFlow_create,
		#"mosse": cv2.TrackerMOSSE_create
    #}

    #grab appropriate obj tracker using dict of opencv obj tracker objects
else:
    tracker = cv2.TrackerCSRT_create() #OPENCV_OBJECT_TRACKERS[args["tracker"]]()

#init bounding box coords of obj to track
initBB = None

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(1.0)

#else, grab ref to vid file
#else:
#    vs = cv2.VideoCapture(args["video"])

#init fps throughput estimator
fps = None

#loop over frames from video stream
while True:
    #grab current frame, then handle if using VideoStream or VideoCapture object
    frame = vs.read()
    #frame = frame [1] if args.get("video", False) else frame

    #check if end of stream reached
    if frame is None:
        break

    #resize frame (faster processing) and retrieve frame dimensions
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    #check if currently tracking object
    if initBB is not None:
        #grab new bounding box coords of object
        (success, box) =  tracker.update(frame)

        #check if tracking was success
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(x, y, w, h)

        #update fps counter
        fps.update()
        fps.stop

        #initialise set of info to display on frame
        info = [
            #("Tracker", args["tracker"]),
            ("Success", "Yes" if success else "No"),
            #("FPS", "{:.2f}".format(fps.fps())),
        ]

        #loop over info tuples and draw on frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    #show output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    #if 's' key is selected, we are going to 'select' a bounding box to track
    #if key == ord("s"):
        #select bounding box of object we want to track (press enter or space after selecting ROI)
    #initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair = True)
    #print(initBB)
    bounding_box_coords, weights = HOGCV.detectMultiScale(frame, winStride = (8,8), padding = (8, 8), scale = 1.03)
    #person = 0
    # for x,y,w,h in bounding_box_coords:
    #     cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
    #     cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    #     person += 1
    #initBB = HOGCV.detectMultiScale(frame, winStride = (8,8), padding = (8, 8), scale = 1.03)

    #start opencv obj tracker using supplied bounding box coords, then start fps throughput estimator
    print(bounding_box_coords, weights)
    if (bounding_box_coords is None):
        initBB = None
    else:
        initBB = bounding_box_coords
        tracker.init(frame, initBB)
    fps = FPS().start()

    #if 'q' key pressed, break loop
    if key == ord("q"):
        break
    
# #if using webcam, release pointer
# if not args.get("video", False):
#     vs.stop()

# #else, release file pointer
# else:
#     vs.release()
vs.stop()

#close all windows
cv2.destroyAllWindows()
 