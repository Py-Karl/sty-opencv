import cv2

img_path = "C:\\Users\\wangx\\Pictures\\Saved Pictures\\lea.jpg"

img = cv2.imread(img_path, -1)
# cv2.namedWindow("IMG GrayScale")
cv2.imshow("IMG GrayScale", img)
key = cv2.waitKey(0) & 0xFF
print(type(key))

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("lea2.jpg", img)
    cv2.destroyAllWindows()


