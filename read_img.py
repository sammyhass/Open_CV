import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("dog.jpg", 0)

cv.imshow("image", img)
cv.imwrite("graydog.png", img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
