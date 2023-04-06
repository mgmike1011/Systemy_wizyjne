'''
Algorytm mieszanin gaussowskich
Bazując na tutorialu:
https://docs.opencv.org/master/d1/dc5/tutorial_background_subtraction.html
Zaimplementować algorytm mieszanin gaussowskich i porównać rezultat działania z wcześniejszymi metodami.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)  # open the default camera

backSub = cv2.createBackgroundSubtractorMOG2()
# Działa znacznie szybciej
while True:
    ret, frame = cap.read()
    fgMask = backSub.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
