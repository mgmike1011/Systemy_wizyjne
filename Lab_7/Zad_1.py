'''

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

thresh = 0
def trackbar_callback(value):
    global thresh
    thresh = value

cap = cv2.VideoCapture(0)  # open the default camera
cv2.namedWindow('background image')
cv2.namedWindow('current image')
cv2.namedWindow('foreground image')
cv2.createTrackbar('Trackbar', 'foreground image', thresh, 255, trackbar_callback)

aktualna_klatka_obrazu = 0
model_tla = 0
model_pierwszego_planu = 0
while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('current image', aktualna_klatka_obrazu)
    cv2.imshow('background image', model_tla)
    cv2.imshow('foreground image', model_pierwszego_planu)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    elif key == ord('a'): # Model tła
        model_tla = img
    elif key == ord('x'): # aktualna klatka obrazu
        aktualna_klatka_obrazu = img
    
    model_pierwszego_planu = cv2.absdiff(model_tla, aktualna_klatka_obrazu)
    ret, model_pierwszego_planu = cv2.threshold(model_pierwszego_planu, thresh, 255, cv2.THRESH_BINARY)

cap.release()
cv2.destroyAllWindows()
