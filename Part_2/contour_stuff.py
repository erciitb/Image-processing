import numpy as np
import cv2

#Capturing a video
cap = cv2.VideoCapture(0)

while True:
    return_val, frame = cap.read()
    #Since the finction findContours always takes a binary image
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    #Contours is an list of points that belong to a particular closed cluster
    im2, contours, hierarchy = cv2.findContours(adaptive_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #For loop for iterating over contours
    for i in range(0, len(contours)):
        cont = contours[i]
        #Calculates all moments
        M = cv2.moments(cont)
        area = cv2.contourArea(cont)
        perimeter = cv2.arcLength(cont, True)
        #Imposing a condition over area and perimeter to reject some noise
        if(M['m00'] and area>100 and perimeter>100):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #Drawing a circle of radius 7 pixels on the center
            cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
            cv2.drawContours(frame, cont, -1, (255, 0, 0), 3)

    cv2.imshow("Showing video", frame)
    cv2.imshow("Showing adaptive threshold", adaptive_thresh)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
