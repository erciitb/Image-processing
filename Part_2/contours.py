import numpy as np
import cv2

#Capture video
cap = cv2.VideoCapture(0)

while True:
    return_val, frame = cap.read()
    #Since the function findContours always takes a binary image
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    #Contours is an array of points that belong to a particular closed cluster
    im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Function draws contours, -1 is to draw all contours. If you want to draw the ith contour, put i there.
    cv2.drawContours(frame , contours, -1, (0, 255, 0), 3)
    cv2.imshow("Showing video", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
