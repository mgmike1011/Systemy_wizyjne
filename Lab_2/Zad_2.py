'''
Wczytaj wybrany przez siebie kolorowy obraz (umieść go w folderze projektu lub podaj ścieżkę absolutną do niego),
    przekonwertuj go do skali szarości, a następnie wykonaj na nim operację progowania binarnego i wyświetl rezultat.
UWAGA Program z poniższych kroków powinien działać w czasie rzeczywistym, tj. zmiana jednego z suwaków powoduje
    zmianę wyświetlanego obrazu wynikowego i nie blokuje wyświetlania obrazu. Wykorzystaj do tego nieskończoną pętlę.
Zmodyfikuj powyższy program tak, aby korzystał z poznanego wcześniej trackbaru (cv2.createTrackbar),
    a wskazywane przez niego wartości zostały użyte jako wartość progowania.
Dodaj kolejny suwak, który umożliwi wybór typu progowania.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Zdj_1.jpg') #Wczytanie zdjęcia
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości


def thresh_callback(value):
    global thresh
    thresh = value


def thresh_type_callback(value):
    global thresh_type
    th = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
    thresh_type = th[value-1]


thresh = 0
thresh_type = cv2.THRESH_BINARY
cv2.namedWindow('Threshold')
cv2.createTrackbar('Thresh', 'Threshold', 0, 255, thresh_callback)
cv2.createTrackbar('Thresh type', 'Threshold', 0, 5, thresh_type_callback)
# Progowanie binarne
while True:
    ret, thresh1 = cv2.threshold(img_grey, thresh, 255, thresh_type)
    cv2.imshow('Threshold', thresh1)
    if cv2.waitKey(10) == ord('q'):
        break
