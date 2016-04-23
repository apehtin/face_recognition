import os
import sys
import cv2

from detection.detector import Detector, Tracker, Player

CUR_PATH = os.getcwd()
RES_PATH = os.getcwd() + '/res/'

DEFAULT_IMAGE = RES_PATH + 'face1.jpg'
DEFAULT_VIDEO = RES_PATH + 'AeroDreamPhone.mp4'
CASCADED_DETECTOR_XML = RES_PATH + 'haarcascade_frontalface.xml'

def main(args):
    if len(args) > 1:
        source = args[1]
    else:
        # Format = Caprturing + camera ID
        source = "Capturing0"

    player = Player(source)
    detector = Detector(CASCADED_DETECTOR_XML)

    player.setProcessing(detector.findFace)

    if player is not None:
        player.run()

    return

if __name__ == "__main__":
    main(sys.argv)
