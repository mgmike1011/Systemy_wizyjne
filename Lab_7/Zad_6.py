'''
Narysować ramkę (cv2.rectangle) dookoła pikseli oznaczonych jako zmienione.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

backSub = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
fgMask = backSub.apply(frame)
last_frame = fgMask.copy()
while True:
    ret, frame = cap.read()
    fgMask = backSub.apply(frame)

    wp = np.sum(fgMask == 255)
    contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        if cv2.contourArea(i) > 250:
            x, y, width, height = cv2.boundingRect(i)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

    last_frame = fgMask.copy()
    cv2.imshow('FG Mask', fgMask)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
