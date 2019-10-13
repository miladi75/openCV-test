import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#Let's presume the Field Of View is equal to 11.3 cm (640px). 
cm_to_pixel = 11.3/640.0


while(1):
    _,frame = cap.read()
    
    gray_image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale using cv2.cvtColor(input, algorithm). doesn't split up components
    
    cv2.imshow('background', gray_image1)

    k = cv2.waitKey(5) 
    if k==27: 
        break

while(1):
    _,frame = cap.read()
    
    gray_image2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    cv2.imshow('foreground', gray_image2)

    difference = np.absolute(np.matrix(np.int16(gray_image1)) - np.matrix(np.int16(gray_image2)))  
    difference[difference>255]=255  
    difference = np.uint8(difference)

    cv2.imshow('Difference',difference)

    BW = difference
    BW[BW<=100]=0
    BW[BW>100]=1

    # Calculate difference column position
    column_sums = np.matrix(np.sum(BW,0))
    column_numbers = np.matrix(np.arange(640))
    column_mult = np.multiply(column_sums,column_numbers) 
    total = np.sum(column_mult)
    total_total = np.sum(np.sum(BW)) 
    column_location = total/total_total

    x_location = column_location * cm_to_pixel  # converts px to cm

    # Calculate difference row position
    row_sums = np.matrix(np.sum(BW,1))  #1 for row
    row_sums = row_sums.transpose()  # to get 480 rows and 1 column
    row_numbers = np.matrix(np.arange(480))
    row_mult = np.multiply(row_sums,row_numbers) 
    total = np.sum(row_mult)
    total_total = np.sum(np.sum(BW)) 
    row_location = total/total_total

    y_location = row_location * cm_to_pixel  # same ratio? usually. Are camera and surface parallell?


    print(x_location, y_location)

    k = cv2.waitKey(5) 
    if k==27: 
        break


cv2.destroyAllWindows()



