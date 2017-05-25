import cv2
from matplotlib import pyplot as plt

img_path = "C:\\Users\\wangx\\Pictures\\Saved Pictures\\fde.jpg"

# img = cv2.imread(img_path, 0)
img = plt.imread(img_path, 0)

# plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
