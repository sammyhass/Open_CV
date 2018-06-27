import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    if ret == True:
        frame_no_blur = cv.flip(frame, 1)
        frame_with_blur = cv.blur(frame_no_blur, (7, 7))
        cv.imshow("Canny Edge Detection", cv.Canny(frame_with_blur, 25, 40))
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
