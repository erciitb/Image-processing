import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    return_val, frame = cap.read()
    #SInce the finction findContours always takes a binary image
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    adaptive_thresh = cv2.medianBlur(adaptive_thresh, 5) # WE applied blurring to remove noise
    #Contours is an list of points that belong to a particular closed cluster

    im2, contours, hierarchy = cv2.findContours(adaptive_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #For loop for iteratong over contours
    for i in range(0, len(contours)):
        cont = contours[i]
        M = cv2.moments(cont)
        area = cv2.contourArea(cont)
        perimeter = cv2.arcLength(cont, True)
        if(M['m00'] and area>200 and perimeter>100):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            eps = 0.1*perimeter
            approx = cv2.approxPolyDP(cont, eps, True)
            #Approx is a list of points that form the vertices of an object
            if(len(approx) == 4):
                cv2.drawContours(frame, cont, -1, (255, 0, 0), 3)
                cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
                approx = np.stack(approx) #Since the polylines finction takes in an array of points, we use np.stack
                cv2.polylines(frame, [approx], True, (0, 255, 255), 4)

    cv2.imshow("Showing video", frame)
    cv2.imshow("Showing adaptive threshold", adaptive_thresh)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
