'''
Policz automatycznie jaka kwota znajduje się na obrazie coins.jpg.
Sumę monet wyświetl w terminalu z dokładnością do 2 miejsc po przecinku, wykorzystując f-string.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg') #6,70zł
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
kwota = 0
th1 = 180
th2 = 220
edges = cv2.Canny(img, th1, th2)

cv2.namedWindow('Image')
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=90, param2=40, minRadius=20, maxRadius=100)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3)
    if i[2] > 50:
        kwota += 100
    else:
        kwota += 10

kwota /= 100
np.round(kwota, 2)
print(f'Wykryta kwota: {kwota} zł')
while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break
