import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    return_val, frame = cap.read()
    cv2.imshow("Showing video", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break