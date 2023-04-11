'''
Śledzenie kolorowych obiektów - wykorzystać poznaną funkcję cv2.inRange
do napisania programu umożliwiającego śledzenie kolorowego obiektu.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    mask = cv2.inRange(frame, np.array([55, 10, 10]), np.array([229, 255, 255]))
    blue = cv2.bitwise_and(frame, frame, mask=mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

    cv2.imshow('Frame', out)
    # cv2.imshow("Frame diff", diff)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
