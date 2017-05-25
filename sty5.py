import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # Connect to the camera of the Laptop

if not cap.isOpened():
    print("open camera.")
    cap.open()

while True:

    ret, frame = cap.read()
    # wid = cap.get(3)
    # hei = cap.get(4)
    # print(wid, hei)
    cap.set(3, 320)
    cap.set(4, 240)
    # print("ret", ret)
    # print("frame", frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
