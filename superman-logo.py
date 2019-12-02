import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([0,108,105],dtype=np.uint8)
    upper_range = np.array([5,186,255],dtype=np.uint8)


    mask = cv2.inRange(hsv, lower_range, upper_range)
    result = cv2.bitwise_and(frame, frame, mask= mask)
    
    cv2.namedWindow('Frame', cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow('Res', cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow('Mask', cv2.WINDOW_KEEPRATIO)


    cv2.imshow('Frame',frame)
    cv2.imshow('Res',result)
    cv2.imshow('Mask',mask)

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()