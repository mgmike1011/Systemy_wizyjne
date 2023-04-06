'''
Napisz program, który umożliwia zaznaczenie dwóch punktów
(będzie to lewy górny róg i prawy dolny pewnego obszaru) i
wykonanie w tym fragmencie obrazu operacji progowania dla kanału G (zielonego).
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.jpg') # Wczytanie zdjęcia
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

points = []
def mouse_callback(event, x, y, flags, param):
    global points, img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
    if len(points) >= 2:
        # cv2.rectangle(img, (points[0][0], points[0][1]), (points[1][0], points[1][1]), (0, 255, 0), -1)
        crop_img = img[points[0][1]:points[1][1], points[0][0]:points[1][0]]
        green_channel = crop_img[:, :, 1]
        ret, thresh3 = cv2.threshold(green_channel, 100, 255, cv2.THRESH_TRUNC)
        crop_img[:, :, 1] = thresh3
        img[points[0][1]:points[1][1], points[0][0]:points[1][0]] = crop_img
        points = []


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('Image',img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()

