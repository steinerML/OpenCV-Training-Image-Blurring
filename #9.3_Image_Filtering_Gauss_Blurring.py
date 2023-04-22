import cv2
import numpy as np

'''We use the GaussianBlur() function that takes 4 arguments:
source: source image, ksize: kernel size, sigmaX and sigmaY: kernel standard
deviations in X and Y direction. Default values are 0, if we set sigmaX to zero, then the standard deviations are computed from the kernel size'''
 
#Read image
image = cv2.imread('test.jpg')

gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0,sigmaY=0)
 
cv2.imshow('Original', image)
cv2.imshow('Gaussian Blurred', gaussian_blur)
     
cv2.waitKey()
cv2.imwrite('gaussian_blur.jpg', gaussian_blur)
cv2.destroyAllWindows()