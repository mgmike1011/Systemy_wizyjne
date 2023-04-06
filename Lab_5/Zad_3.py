'''
Napisz program wykrywający w obrazie linie proste oraz okręgi
(wykorzystać funkcje HoughLines, HoughLinesP, HoughCircles).
Do testów można wykorzystać obraz shapes.jpg.
Jako wzór wykorzystaj tutorial dla linii oraz dla okręgów.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('shapes.jpg')
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th1 = 160
th2 = 200
edges = cv2.Canny(img, th1, th2)

lines = cv2.HoughLines(edges, 1, np.pi/180, 120)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40, minRadius=20, maxRadius=250)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break
