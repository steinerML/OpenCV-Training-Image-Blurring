import cv2
import numpy as np

'''We use the filter2D() function to define different kernels according to
the theoretical definition (https://en.wikipedia.org/wiki/Kernel_(image_processing))

For instance a sharpening kernel: [[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]]'''
 
#Read image
image = cv2.imread('test.jpg')

#Define kernel
kernel3 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

#Define arguments for filter2D()
sharpened = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharpened)

cv2.waitKey()
cv2.imwrite('sharpened.jpg', sharpened)
cv2.destroyAllWindows()