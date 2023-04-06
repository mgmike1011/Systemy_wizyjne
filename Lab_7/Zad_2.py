'''
Algorytm przybliżonej mediany
Zaimplementować algorytm przybliżonej mediany na podstawie schematu blokowego przedstawionego we wstępie.
UWAGA: Przyjąć pierwszą klatkę obrazu jako początkowy model tła.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

thresh = 15
def trackbar_callback(value):
    global thresh
    thresh = value

cv2.namedWindow('Image')
cv2.createTrackbar('Trackbar', 'Image', thresh, 255, trackbar_callback)

cap = cv2.VideoCapture(0)  # open the default camera
ret, B = cap.read()
B = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    I = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    D = cv2.absdiff(B, I)
    ret, D_prim = cv2.threshold(D, thresh, 255, cv2.THRESH_BINARY)

    B_poprzedni = B.copy()

    B[B_poprzedni < I] += 1
    B[B_poprzedni > I] -= 1

    cv2.imshow('Image', D_prim)
    I_poprzedni = I
    B_poprzedni = B
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
