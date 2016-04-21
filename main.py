import os
import sys
import cv2

from detection.detector import Detector, Tracker

CUR_PATH = os.getcwd()
RES_PATH = os.getcwd() + '/res/'

DEFAULT_IMAGE = RES_PATH + 'face1.jpg'
CASCADED_DETECTOR_XML = RES_PATH + 'haarcascade_frontalface.xml'

def main(args):
    if len(args) > 1:
        source = args[1]
    else:
        source = DEFAULT_IMAGE

    img = cv2.imread(source, cv2.IMREAD_COLOR)

    detector = Detector(CASCADED_DETECTOR_XML)
    faces = detector.findFace(img)

    cv2.namedWindow(source, cv2.WINDOW_NORMAL)
    cv2.imshow(source, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    main(sys.argv)
