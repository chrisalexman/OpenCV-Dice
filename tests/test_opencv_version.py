"""
This test checks the OpenCV version.
TODO: convert to Python unittest framework ?
"""

import cv2 as cv

if __name__ == '__main__':
    print("cv2 version: {}".format(cv.__version__))
