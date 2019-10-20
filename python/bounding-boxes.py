import cv2 as cv
import numpy as np


img = cv.pyrDown(cv.imread('/home/silje/Pictures/man-mountain.jpg',cv.IMREAD_UNCHANGED)) #load in color

red = np.matrix(img[:,:,2])  
green = np.matrix(img[:,:,1])
blue = np.matrix(img[:,:,0])

red_only = np.int16(red) - np.int16(green) - np.int16(blue) # np.int16() gives us values in int16, so that our code can handle negative values # ranges from -255 to 255, 16 bits.

red_only[red_only<0] = 0  # every element < 0, becomes 0, such that it becomes a valid image matrix.
red_only[red_only>0] = 255 # basically saturation
red_only = np.uint8(red_only) # represent as uint8, because everything between 0-255

#FINDING CONTOURS
ret, threshed_img = cv.threshold(cv.cvtColor(img, cv.COLOR_BGR2GRAY),30, 255, cv.THRESH_BINARY_INV)
contours_th, hier = cv.findContours(threshed_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #creates a list contours
contours_red, hier = cv.findContours(red_only, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #creates a list contours

#DRAWING BOXES
for c in contours_th:
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img, (x, y), (x+w, y+h),(0,255,0),2)
for c in contours_red:
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img, (x, y), (x+w, y+h),(255,0,0),2)


cv.imshow('red',red_only)
cv.imshow("normal",img)
cv.imshow("thresh",threshed_img)

while True:
    key = cv.waitKey(1)
    if key == 27: #ESC key to break
        break

cv.destroyAllWindows()