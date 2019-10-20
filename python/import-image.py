import numpy as np
import cv2

# Load a color image in color
img = cv2.imread('/home/silje/Pictures/path-marker.jpg',1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL) #Resize window
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('newimage.png',img)
    cv2.destroyAllWindows()