'''
Zapoznaj się z adaptacyjnym progowaniem (sekcja Adaptive thresholdng): https://docs.opencv.org/5.x/d7/d4d/tutorial_py_thresholding.html.
'''
import cv2

img = cv2.imread('Zdj_1.jpg') #Wczytanie zdjęcia
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości

th1 = cv2.adaptiveThreshold(img_grey,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(img_grey,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Adaptive Mean', th1)
cv2.imshow('Adaptive Gaussian', th2)

while True:
    if cv2.waitKey(10) == ord('q'):
        break
