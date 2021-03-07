import numpy as np
import cv2

#Reading an image
image = cv2.imread("noise.jpg", 1)

#Resizing the image because it is huge!
image = cv2.resize(image, (500, 500))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)
dilate = cv2.dilate(image, kernel, iterations = 1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow('image', image)
cv2.imshow('erosion', erosion)
cv2.imshow('dilate', dilate)
cv2.imshow('opening', opening)

k = cv2.waitKey(0)
if k == 95:
    cv2.destroyAllWindows()

