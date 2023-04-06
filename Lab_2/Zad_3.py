'''
Pobierz obraz sześcianu. Wczytaj go i przeskaluj go "w górę", zwiększając jego rozdzielczość 2.75x.
Nie korzystając z trackbara, wypróbuj różne metodami interpolacji
(cv2.INTER_LINEAR, cv2.INTER_NEAREST, cv2.INTER_AREA, cv2.INTER_LANCZOS4)
i wyświetl je w osobnych oknach. Zwróć uwagę na różnice w jakości obrazu.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('qr.jpg') # Wczytanie zdjęcia
img_scaled_linear = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR) # Przeskalowanie obrazu
img_scaled_inter_nearest = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST) # Przeskalowanie obrazu
img_scaled_area = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA) # Przeskalowanie obrazu
img_scaled_lanczos = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4) # Przeskalowanie obrazu

cv2.imshow('Scaled Linear', img_scaled_linear)
cv2.imshow('Scaled Nearest', img_scaled_inter_nearest)
cv2.imshow('Scaled Area', img_scaled_area)
cv2.imshow('Scaled Lanczos', img_scaled_lanczos)

while True:
    if cv2.waitKey(10) == ord('q'):
        break
