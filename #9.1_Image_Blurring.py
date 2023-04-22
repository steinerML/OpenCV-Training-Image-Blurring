import cv2
import numpy as np

'''We use the filter2D function that takes 3 arguments:
source: source image, ddepth: indicates the depth of resulting image
and kernel, which we apply to the image'''
 
#Read image
image = cv2.imread('test.jpg')

#Define 5x5 kernel and normalize it by dividing by the num. elements in kernel
kernel2 = np.ones((5, 5), np.float32) / 25

#Define arguments for filter2D()
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
identity = cv2.blur(src=image, ksize=(5,5))

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()