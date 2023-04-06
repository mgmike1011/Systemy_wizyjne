'''
Zapoznaj się z histogramami w opencv https://docs.opencv.org/5.x/d1/db7/tutorial_py_histogram_begins.html, a następnie wykonaj kroki:
Wyświetl histogram dla swojego obrazu, zarówno w skali szarości, jak i dla obrazu kolorowego.
    Uwaga:
    Do wyznaczania histogramu użyć funkcji OpenCV - cv2.calcHist, natomiast do wyświetlania bibliotekę matplotlib.
Wykonaj operację wyrównania histogramu (do fragmentu CLAHE (Contrast Limited Adaptive Histogram Equalization))
    opisaną w: https://docs.opencv.org/5.x/d5/daf/tutorial_py_histogram_equalization.html.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.jpg') # Wczytanie zdjęcia
img = cv2.resize(img,(0, 0), fx=0.5, fy=0.5)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([img_grey],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256]); plt.show()
plt.title("Histogram skala szarosci")

color = ('b','g','r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])
plt.title("Histogram kolor")
plt.show()

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_grey)
cv2.imshow("Clache", cl1)
key = cv2.waitKey(0)