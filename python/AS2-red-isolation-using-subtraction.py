import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read() #
    
    red = np.matrix(frame[:,:,2])  
    green = np.matrix(frame[:,:,1])
    blue = np.matrix(frame[:,:,0])
    
    red_only = np.int16(red) - np.int16(green) - np.int16(blue) # np.int16() gives us values in int16, so that our code can handle negative values
    # ranges from -255 to 255, 16 bits.

    red_only[red_only<0] = 0  # every element < 0, becomes 0, such that it becomes a valid image matrix.
    red_only[red_only>255] = 255 # basically saturation
    red_only = np.uint8(red_only) # represent as uint8, because everything between 0-255

    cv2.imshow('rgb',frame)
    cv2.imshow('red',red)
    cv2.imshow('green',green)
    cv2.imshow('blue',blue)
    cv2.imshow('red only',red_only) # most colors turn black, except for red

    k = cv2.waitKey(5) 
    if k==27: 
        break
cv2.destroyAllWindows()

print(red_only)