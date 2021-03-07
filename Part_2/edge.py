import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    return_val, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image, 100, 200)
    cv2.imshow("Showing video", edges)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
