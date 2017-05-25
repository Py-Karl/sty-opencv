import numpy as np
import cv2

img_path = "C:\\Users\\wangx\\Desktop\\8.png"
img = cv2.imread(img_path)      # img Type is <class 'numpy.ndarray'>

# print(img)
# print(type(img))
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)

# cv2.imwrite("2.png", img)

cv2.destroyAllWindows()
