face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



#####################################
#Please remember to return value to
   
def detect_face_false_thermal(argv):
    cap = cv2.VideoCapture(0)
    person = 0
    #initialize the colormap
    colormap = mpl.cm.jet
    cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
    scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)


    while (True):
import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#########face detection#############################
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
            faces = 1
            return "stopservo"
        
##### thermal ##################################
        # Our operations on the frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #if want blur
		#add blur to make it more realistic
        blur = cv2.GaussianBlur(gray,(15,15),0)
		#assign colormap
        colors = scalarMap.to_rgba(blur, bytes=False)


        # no blur (uncomment this section and comment the other one)
        #colors = scalarMap.to_rgba(gray)

        # Display the resulting frame
        cv2.imshow('frame', colors)

        #stop with esc key
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
         
    cap.release()
    cv2.destroyAllWindows()


