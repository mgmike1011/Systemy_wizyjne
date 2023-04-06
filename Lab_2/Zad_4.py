'''
Wykonaj operację mieszania dwóch obrazów (blending). Wykorzystaj wybrany przez siebie obraz oraz logo Laboratorium Systemów Wizyjnych.
Skorzystaj z trackbaru do określenia wartości parametrów alpha oraz beta. Sprawdź, co oznacza saturated operation.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_1 = cv2.imread('PUTVISION_LOGO.png')
img_1_dim = img_1.shape
img_2 = cv2.imread('Zdj_1.jpg')
img_2 = cv2.resize(img_2, dsize=(img_1_dim[0], img_1_dim[1])) #Skalowanie do takiej samej rozdzielczości


def alpha_callback(value):
    global alpha
    alpha = value/100


def beta_callback(value):
    global beta
    beta = value/100


alpha = 1
beta = 1
cv2.namedWindow('Blend')
cv2.createTrackbar('alpha', 'Blend', 0, 100, alpha_callback)
cv2.createTrackbar('beta', 'Blend', 0, 100, beta_callback)

while True:
    img_blend = cv2.addWeighted(img_1, alpha, img_2, beta, 0)
    cv2.imshow('Blend', img_blend)
    if cv2.waitKey(10) == ord('q'):
        break
