import numpy as np
import cv2 as cv

vid=cv.VideoCapture(0)

while vid.isOpened():
    ret, frames=vid.read()

    if not ret:
        print('ERROR')
        break

    cv.imshow('video',frames)
    if cv.waitKey(1)=='e':
        break

vid.release()
cv.destroyAllWindows()