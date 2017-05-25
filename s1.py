import cv2
import numpy as np

image_path = "lea2.jpg"

img = cv2.imread(image_path)
img_n = img[248:300, 245:300]       # extract a region
# cv2.namedWindow('image', 0)
cv2.imshow('image', img_n)
cv2.waitKey(0)

# img1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#
# cv2.imshow('img1', img1)
# cv2.waitKey(0)


cv2.destroyAllWindows()
