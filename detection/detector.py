import cv2

class Tracker():
    def __init__(self):
        return


class Detector():
    def __init__(self, cascPath):
        self.faceCascade = cv2.CascadeClassifier(cascPath)
        return

    def findFace(self, img, draw = True):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

        if draw:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

        return faces