import sys
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_detect(argv):
    cap = cv2.VideoCapture(0)
    face_detected= False
    while (True):
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
            print("face detected")
            face_detected = True
        if face_detected == True:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(face_detect(sys.argv))
