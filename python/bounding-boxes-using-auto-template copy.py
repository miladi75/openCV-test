import cv2 as cv
import numpy as np

def findAndReturnROI(c_vec, c_img):
    c_max = max(c_vec, key = cv.contourArea) #Maximum contour area, draw it
    x, y, w, h = cv.boundingRect(c_max)
    ROI = c_img[y:y+h, x:x+w]  # cropping from red_only
    cv.imwrite('ROI1.jpg',ROI)  #saving to file
    temp = cv.imread('ROI1.jpg',0)
    return temp

def bgrMatrices(img):
    red = np.matrix(img[:,:,2])  
    green = np.matrix(img[:,:,1])
    blue = np.matrix(img[:,:,0])
    return blue,green,red

def templateComparison(img, template, original):
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        method = eval(meth)

        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
           top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        #display in original image
        cv.rectangle(original,top_left, bottom_right, (0,0,255), 2)
        cv.imshow(meth,original)

def subtractAndSaturate(targetM, m1, m2):
    sub_output = np.int16(targetM) - np.int16(m1) - np.int16(m2)
    sub_output[sub_output<0] = 0  
    sub_output[sub_output>0] = 255
    sub_output = np.uint8(sub_output)
    return sub_output



#MAIN
img = cv.pyrDown(cv.imread('/home/silje/Pictures/man-mountain.jpg',cv.IMREAD_UNCHANGED)) 

blue,green,red = bgrMatrices(img)

red_only = subtractAndSaturate(red,green,blue)

#FINDING CONTOURS
ret, threshed_img = cv.threshold(cv.cvtColor(img, cv.COLOR_BGR2GRAY),10, 255, cv.THRESH_BINARY_INV)
contours_th, hier = cv.findContours(threshed_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
contours_red, hier = cv.findContours(red_only, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 

#finding ROI
temp = findAndReturnROI(contours_th,threshed_img)
w,h = temp.shape[::-1] #width, height of temp image

templateComparison(threshed_img,temp,img)

cv.imshow('red',red_only)
cv.imshow("normal",img)
cv.imshow("thresh",threshed_img)

while True:
    key = cv.waitKey(1)
    if key == 27: #ESC key to break
        break

cv.destroyAllWindows()