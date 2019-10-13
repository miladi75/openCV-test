import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read() #
    
    red = np.matrix(frame[:,:,2])  
    green = np.matrix(frame[:,:,1])
    blue = np.matrix(frame[:,:,0])
    
    red_only = np.int16(red) - np.int16(green) - np.int16(blue)

    red_only[red_only<0] = 0 
    red_only[red_only>255] = 255

    column_sums = np.matrix(np.sum(red_only,0))  # np.sum: 0 - sum columns, 1 -sum rows
    column_numbers = np.matrix(np.arange(640)) # np.aRange: list of numbers from 1 to 640
    column_mult = np.multiply(column_sums,column_numbers) # np.multiply: element wise multiplication, same dimension as input
    total = np.sum(column_mult) # no axis?
    total_total = np.sum(np.sum(red_only)) # inside-sum will sum columns in red_only, outside-sum will take sum of sums
    column_location = total/total_total

    # Explanation: Center of brightness. column sums times row number. sum this. divide by total sum of values.

    print(column_location)  # from 0 to 640

    red_only = np.uint8(red_only)

    cv2.imshow('rgb',frame)
    cv2.imshow('red',red)
    cv2.imshow('green',green)
    cv2.imshow('blue',blue)
    cv2.imshow('red only',red_only) 

    k = cv2.waitKey(5) 
    if k==27: 
        break
cv2.destroyAllWindows()

print(red_only)