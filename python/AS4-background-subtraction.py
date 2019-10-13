import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    
    gray_image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale using cv2.cvtColor(input, algorithm). doesn't split up components
    
    cv2.imshow('background', gray_image1)

    k = cv2.waitKey(5) 
    if k==27: 
        break

while(1):
    _,frame = cap.read()
    
    gray_image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale using cv2.cvtColor(input, algorithm). doesn't split up components
    
    cv2.imshow('foreground', gray_image2)

    difference = np.absolute(np.matrix(np.int16(gray_image1)) - np.matrix(np.int16(gray_image2)))  # don't know if object is brighter or darker than background, therefore absolute value.
    difference[difference>255]=255  #don't need el < 0 because we have already done the absolute value
    difference = np.uint8(difference)

    cv2.imshow('Difference',difference)

    k = cv2.waitKey(5) 
    if k==27: 
        break


cv2.destroyAllWindows()

# Calculate difference column position
column_sums = np.matrix(np.sum(difference,0))
column_numbers = np.matrix(np.arange(640))
column_mult = np.multiply(column_sums,column_numbers) 
total = np.sum(column_mult)
total_total = np.sum(np.sum(difference)) 
column_location = total/total_total

print(column_location)

