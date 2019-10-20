import cv2 as cv
import numpy as np

img = cv.pyrDown(cv.imread('/home/silje/Pictures/man-mountain.jpg',cv.IMREAD_UNCHANGED)) 
temp = cv.imread('/home/silje/Pictures/temp.jpg',0) #Load template image
w,h = temp.shape[::-1] #width, height of temp image


red = np.matrix(img[:,:,2])  
green = np.matrix(img[:,:,1])
blue = np.matrix(img[:,:,0])

red_only = np.int16(red) - np.int16(green) - np.int16(blue)

red_only[red_only<0] = 0  
red_only[red_only>0] = 255
red_only = np.uint8(red_only)

#FINDING CONTOURS
ret, threshed_img = cv.threshold(cv.cvtColor(img, cv.COLOR_BGR2GRAY),30, 255, cv.THRESH_BINARY_INV)
contours_th, hier = cv.findContours(threshed_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
contours_red, hier = cv.findContours(red_only, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    method = eval(meth)

    # Apply template Matching
    res = cv.matchTemplate(threshed_img,temp,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(img,top_left, bottom_right, (0,0,255), 2)
    cv.imshow(meth,img)

cv.imshow('red',red_only)
cv.imshow("normal",img)
cv.imshow("thresh",threshed_img)

while True:
    key = cv.waitKey(1)
    if key == 27: #ESC key to break
        break

cv.destroyAllWindows()