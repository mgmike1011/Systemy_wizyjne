'''
Napisz program umożliwiający wczytanie pliku graficznego w skali szarości, a następnie obliczenie pochodnych
cząstkowych za pomocą maski Prewitta i Sobela (należy wykorzystać funkcję cv2.filter2D).
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gallery.png') # Wczytanie zdjęcia
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Prewitt
Mx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
My = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
img_prewittx = np.abs(cv2.filter2D(img_grey, cv2.CV_32F, Mx) / 3.0)
img_prewitty = np.abs(cv2.filter2D(img_grey, cv2.CV_32F, My) / 3.0)
img_prewittx_max = np.amax(img_prewittx)
img_prewitty_max = np.amax(img_prewitty)
img_prewittx = img_prewittx / img_prewittx_max * 255 #Przeskalowanie 0...2555
img_prewitty = img_prewitty / img_prewitty_max * 255

#Sobel
Mx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
My = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
img_sobelx = np.abs(cv2.filter2D(img_grey, cv2.CV_32F, Mx) / 4.0)
img_sobely = np.abs(cv2.filter2D(img_grey, cv2.CV_32F, My) / 4.0)
img_sobelx_max = np.amax(img_sobelx)
img_sobely_max = np.amax(img_sobely)
img_sobelx = img_sobelx / img_sobelx_max * 255 #Przeskalowanie 0...2555
img_sobely = img_sobely / img_sobely_max * 255

# Obraz modułu gradientu
M_xy_prewitt = np.sqrt((cv2.filter2D(img_grey, cv2.CV_32F, Mx) / 3.0)**2 + (cv2.filter2D(img_grey, cv2.CV_32F, My) / 3.0)**2)
M_xy_sobel = np.sqrt((cv2.filter2D(img_grey, cv2.CV_32F, Mx) / 4.0)**2 + (cv2.filter2D(img_grey, cv2.CV_32F, My) / 4.0)**2)

cv2.imshow('Image', img_grey)
cv2.imshow('Image_Prewit_X', img_prewittx.astype(np.uint8))
cv2.imshow('Image_Prewit_y', img_prewitty.astype(np.uint8))
cv2.imshow('Image_Sobel_X', img_sobelx.astype(np.uint8))
cv2.imshow('Image_Sobel_y', img_sobely.astype(np.uint8))
cv2.imshow('Gradiend Sobel', M_xy_sobel.astype(np.uint8))
key = cv2.waitKey(0)
