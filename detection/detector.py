import cv2

class Tracker():
    def __init__(self):
        return


class Player():
    def __init__(self, source):
        self.image = False
        self.video = False
        self.capture = False
        self.processing = False
        self.sourceName = source
        self.__procFunc = None

        if source[:9] == 'Capturing':
            self.capture = True
            camNumber = source[9:]

            try:
                self.camNumber = int(camNumber)
            except ValueError:
                print 'Invalid camera ID:', camNumber
                return

            try:
                self.__source = cv2.VideoCapture(self.camNumber)
            except Exception:
                print 'There is no camera with ID:', self.camNumber
                return

        else:
            image = (source[-4:] == '.jpg' or
                     source[-4:] == '.png' or
                     source[-4:] == 'jpeg')

            video = (source[-4:] == 'mpeg' or
                     source[-4:] == '.mpg' or
                     source[-4:] == '.mp4' or
                     source[-4:] == '.avi')

            if image:
                try:
                    self.__source = cv2.imread(source, cv2.IMREAD_COLOR)
                    self.image = True
                except Exception:
                    print "Can't read image:", source
                    return

            elif video:
                try:
                    self.__source = cv2.VideoCapture(source)
                    self.video = True
                except Exception:
                    print "Can't read video:", source
                    return

            else:
                print "Invalid format for Player():", source

        return

    def setProcessing(self, procFunc):
        self.__procFunc = procFunc
        self.processing = True
        return

    def run(self):
        cv2.namedWindow(self.sourceName, cv2.WINDOW_NORMAL)

        if self.image:
            if self.processing:
                frame, _ = self.__procFunc(self.__source)

            cv2.imshow(self.sourceName, frame)
            cv2.waitKey(0)

        if self.video:
            while(self.__source.isOpened()):
                ret, frame = self.__source.read()

                if self.processing:
                    frame, _ = self.__procFunc(frame)

                cv2.imshow(self.sourceName, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            self.__source.release()

        if self.capture:
            while(True):
                ret, frame = self.__source.read()

                if self.processing:
                    frame, _ = self.__procFunc(frame)

                cv2.imshow(self.sourceName, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            self.__source.release()

        cv2.destroyAllWindows()
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

        return img, faces