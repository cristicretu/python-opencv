import numpy as np
import cv2

img = cv2.imread(
    '/home/cristic/Projects/python-opencv/assets/watch.jpeg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)

cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'YES', (0, 130), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
