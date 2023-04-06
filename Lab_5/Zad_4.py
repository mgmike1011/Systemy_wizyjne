'''
Napisz program, który możliwie dobrze nakreśli granice statku
na zdjęciu dla autonomicznie lądującej rakiety. Wykorzystaj jako wejście obraz drone_ship.jpg.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('drone_ship.jpg')

th1 = 180
th2 = 220
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
circles = cv2.HoughCircles( #Zwraca x y i radius
    edges, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=65, minRadius=40, maxRadius=250
)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3)


while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break
