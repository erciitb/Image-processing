import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    return_val, frame = cap.read()
    #SInce the finction findContours always takes a binary image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([110,50,50]) #Defining lower range
    upper = np.array([130, 255, 255]) #DEfining upper limit
    mask = cv2.inRange(hsv, lower, upper) #Using the inRange function to give a binary mask
    mask = cv2.medianBlur(mask, 5) # WE applied blurring to remove nouse
    #Contours is an list of points that belong to a particular closed cluster

    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #For loop for iteratong over contours
    for i in range(0, len(contours)):
        cont = contours[i]
        M = cv2.moments(cont)
        area = cv2.contourArea(cont)
        perimeter = cv2.arcLength(cont, True)
        if(area>200 and perimeter>100):
            ellipse = cv2.fitEllipse(cont)
            #This function returns (x, y) of center, (major and minor axis) and angle of tilt ((x,y), (M, m), angle)
            Ma, ma = ellipse[1]
            if(abs(Ma-ma)<10.55):
                (x,y), radius = cv2.minEnclosingCircle(cont)
                center = (int(x), int(y))
                cv2.circle(frame, center, int(radius), (255, 0, 0), 3)


    cv2.imshow("Showing video", frame)
    cv2.imshow("Showing adaptive threshold", mask)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break