'''
Napisz program oznaczający automatycznie pomarańcze i jabłka dla sortowni owoców. Wykorzystaj jako wejście
obraz fruit.jpg. Dla robota zbierającego wystarczy, że owoce dwóch rodzajów będą otoczone obwódkami w różnych kolorach.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fruit.jpg')

th1 = 180
th2 = 220
edges = cv2.Canny(img, th1, th2)

circles = cv2.HoughCircles( #Zwraca x y i radius
    edges, cv2.HOUGH_GRADIENT, 1, 50, param1=80, param2=30, minRadius=100, maxRadius=170
)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    width = round(i[2] / np.sqrt(2))

    hsv_area = cv2.cvtColor(
        img[i[1] - width: i[1] + width, i[0] - width: i[0] + width],
        cv2.COLOR_BGR2HSV,
    )
    mean_h = np.mean(hsv_area[:, :, 0])

    if mean_h < 20:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 4)
    elif mean_h > 25:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 4)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break