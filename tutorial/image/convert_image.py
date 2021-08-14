"""
This code takes a .jpg image and converts it to a .png image.
- opens from /input/starry_night.jpg
- displays .jpg image on screen, waits for 's' keypress
- saves to /input/starry_night.png
"""

import cv2 as cv
import sys


def convert_image():
    img_input_path = "/home/pi/Documents/opencv-dice/tutorial/input/starry_night.jpg"
    img_output_path = "/home/pi/Documents/opencv-dice/tutorial/output/starry_night.png"

    img = cv.imread(img_input_path)

    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)

    k = cv.waitKey(0)

    if k == ord('s'):
        cv.imwrite(img_output_path, img)


if __name__ == "__main__":
    convert_image()
