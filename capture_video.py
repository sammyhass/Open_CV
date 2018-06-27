import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read() # read the current frame
    if ret == True:
        frame_to_use = cv.flip(frame, 1)
        cv.imshow("frame", frame_to_use) # mirror the frame
        out.write(frame_to_use)
        if cv.waitKey(1) & 0xFF == ord("q"): # check if user presses letter 'q'
            break

cap.release() # Stop Recording
out.release() # Stop saving video
cv.destroyAllWindows() # Close window
