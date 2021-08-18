"""

"""

import cv2 as cv


def find_dice():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        edges_wide = cv.Canny(blur, 10, 200)
        edges_mid = cv.Canny(blur, 30, 150)
        edges_tight = cv.Canny(blur, 240, 250)

        # Display the resulting frame
        cv.imshow('frame1', edges_wide)
        cv.imshow('frame2', edges_mid)
        cv.imshow('frame3', edges_tight)

        # TODO: create trackbar and functions

        if cv.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    find_dice()
