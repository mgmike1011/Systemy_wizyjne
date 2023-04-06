'''
Wykorzystując program z poprzednich zajęć, który wykonywał operację progowanie binarnego,
    wykonaj na obrazie binarnym jedną z operacji cv2.erode lub cv2.dilate. Wyświetl w osobnych oknach obraz po samej
    operacji progowania, a w osobnym obraz po progowaniu i operacji morfologicznej.
Dodaj trackbar, który umożliwia sterowanie rozmiarem maski wykorzystywanej w operacji morfologicznej.
    Zaobserwuj efekt jej zmiany.
Po przetestowaniu erozji i dylacji przetestuj otwarcie i domknięcie.
    Zastanów się, kiedy przydatna może być operacja domknięcia, a kiedy otwarcia.
'''
import cv2
import numpy as np


def thresh_callback(value):
    global thresh
    thresh = value


def erosion_callback(value):
    global kernel
    kernel = np.ones((value, value), np.uint8)


img = cv2.imread('lenna_noise.bmp')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości
thresh = 0
kernel = np.ones((5, 5), np.uint8)

thresh_type = cv2.THRESH_BINARY
cv2.namedWindow('Control')
cv2.createTrackbar('Thresh', 'Control', 0, 255, thresh_callback)
cv2.createTrackbar('Kernel', 'Control', 0, 100, erosion_callback)

while True:
    ret, thresh1 = cv2.threshold(img_grey, thresh, 255, thresh_type)
    erosion = cv2.erode(thresh1, kernel, iterations=1)
    opening = cv2.morphologyEx(img_grey, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img_grey, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Threshold', thresh1)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    if cv2.waitKey(10) == ord('q'):
        break
