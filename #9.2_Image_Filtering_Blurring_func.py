import cv2
import numpy as np

'''We use the blur() function that takes 2 arguments:
source: source image, ksize: kernel size'''
 
#Read image
image = cv2.imread('test.jpg')

#In this case the kernel definition is inside the blur() function.
#It will produce the same output as filter2d()

#Define arguments for blur(). Kernel size 5 x 5
blur = cv2.blur(src=image, ksize=(5,5))

cv2.imshow('Original', image)
cv2.imshow('Blurred', blur)

cv2.waitKey()
cv2.imwrite('blur.jpg', blur)
cv2.destroyAllWindows()