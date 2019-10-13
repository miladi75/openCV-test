import numpy as np
import cv2

cap = cv2.VideoCapture(0) #number indicates which camera to use

while(1):
    _,frame = cap.read() # _ because we need another variable to indicate success/failure
    
    red = frame[:,:,2]  # : -takes all of rows,columns. third layer = index 2.
    green = frame[:,:,1]
    blue = frame[:,:,0]
    
    cv2.imshow('rgb',frame)
    cv2.imshow('red',red)
    cv2.imshow('green',green)
    cv2.imshow('blue',blue)

    k = cv2.waitKey(5)  # check if exit key kressed
    if k==27: # code for the esc key
        break
cv2.destroyAllWindows()

print(frame)
print(frame.shape) #(rows, columns, layers) resolution = pix.
#all numbers are 8-bit values. 0-255. 8-bit depth
#the 3: color space. three matrices with each res, one about red, one about blue, one about green.