import cv2
import numpy as np

'''We use the medianBlur() function that takes 2 arguments:
source: source image, ksize: kernel size must be an integer, not a tuple
as in the Gaussian Blur. Given the same kernel size there is more blur in the Median blurring than in the Gaussian'''
 
#Read image
image = cv2.imread('test.jpg')

median_blur = cv2.medianBlur(src=image, ksize=5)
 
cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median_blur)
     
cv2.waitKey()
cv2.imwrite('median_blur.jpg', median_blur)
cv2.destroyAllWindows()