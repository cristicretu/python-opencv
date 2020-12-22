import cv2
import numpy as np

img = cv2.imread('/home/cristic/Projects/python-opencv/assets/bookpage.jpeg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive = cv2.adaptiveThreshold(
    grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval, threshold = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)

cv2.imshow('original', img)
cv2.imshow('Adaptive threshold', adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
