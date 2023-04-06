'''

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gallery.png')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości
th1 = 0
th2 = 0

def th1_callback(value):
    global th1
    th1 = value

def th2_callback(value):
    global th2
    th2 = value

cv2.namedWindow('Image')
cv2.createTrackbar('th1', 'Image', 0, 255, th1_callback)
cv2.createTrackbar('th2', 'Image', 0, 255, th2_callback)

while True:
    edges = cv2.Canny(img_grey, th1, th2)
    cv2.imshow('Image', edges)
    if cv2.waitKey(10) == ord('q'):
        break
