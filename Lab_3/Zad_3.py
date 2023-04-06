'''
Wczytaj dowolny obraz w skali szarości, korzystając z pętli, przeiteruj po obrazie i co trzeci piksel w wierszu zamień na biały (wartość 255).
Napisz program, który wykona na powyższym obrazie operację wygładzania w oknie 3x3 w krokach:
        zsumuj wszystkie piksele z wiersza nad/pod oraz kolumny przed/po
        podziel sumę przez liczbę pikseli (9).
Program powinien pominąć pierwszy/ostatni wiersz oraz pierwszą/ostatnią kolumnę.
Porównaj czas wykonywania oraz jakość działania z wbudowaną funkcją cv2.blur(src, (3, 3)).
Porównać czas wykonania oraz jakość działania z realizacją uśredniania za pomocą funkcji cv2.filter2D.
'''
import time
import cv2
import numpy as np
from time import perf_counter

img = cv2.imread('lenna_noise.bmp')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości

for i in range(img_grey.shape[0]):
    for j in range(img_grey.shape[1]):
        if j%3 == 0:
            img_grey[i, j] = 255

def filter(img):
    img_out = np.zeros(img.shape,dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i == 0 or i == (img.shape[0]-1) or j == 0 or j == (img.shape[1]-1):
                img_out[i, j] = img[i, j]
            else:
                wiersz_nad = np.sum(img[i-1, j])
                wiersz_pod = np.sum(img[i+1, j])
                kolumna_przed = np.sum(img[i, j-1])
                kolumna_za = np.sum(img[i, j+1])
                usrednienie = (wiersz_nad + wiersz_pod + kolumna_za + kolumna_przed)/9
                img_out[i, j] = usrednienie
    return img_out

t_start = time.perf_counter()
img_filter = filter(img_grey)
t_stop = time.perf_counter()
print(f'Filter: {t_stop-t_start} s')
cv2.imshow('Filter', img_filter)

t_start = time.perf_counter()
img_blur = cv2.blur(img_grey, (3, 3))
t_stop = time.perf_counter()
print(f'CV2 Blur: {t_stop-t_start} s')

kernel1 = np.ones((3, 3), np.float32)/30
t_start = time.perf_counter()
img_2d = cv2.filter2D(img_grey, ddepth=-1, kernel=kernel1)
t_stop = time.perf_counter()
print(f'CV2 fiter 2D: {t_stop-t_start} s')

cv2.imshow('Img', img_grey)
cv2.imshow('Blur', img_blur)
cv2.imshow('2D', img_2d)
cv2.imshow('Filter', img_filter)

while True:
    if cv2.waitKey(10) == ord('q'):
        break
