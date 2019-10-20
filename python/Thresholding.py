import cv2 as cv
import numpy as np
v = 127  #Thresholding value
imgr = cv.imread('/home/silje/Pictures/man-mountain.jpg',0)
img = cv.blur(imgr,(3,3))

ret,thresh1 = cv.threshold(img,v,255,cv.THRESH_BINARY)  # ret is whether or not the operation is successfull
ret,thresh2 = cv.threshold(img,v,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,v,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,v,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,v,255,cv.THRESH_TOZERO_INV)
blur = cv.GaussianBlur(img,(5,5),0)
ret,thresh6 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
imgb = cv.medianBlur(img,5)
th2 = cv.adaptiveThreshold(imgb,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(imgb,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','otsu','adaptive mean','adaptive gaussian']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6,th2,th3]
for i in range(9):
    imS = cv.resize(images[i], (500, 300)) 
    cv.namedWindow(titles[i], cv.WINDOW_NORMAL)
    cv.imshow(titles[i],imS)

k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()