'''
Wykonywanie wielu operacji na tak dużych macierzach jak obrazy może być czasochłonne.
W celu wyznaczenia czasu trwania fragmentu programu można skorzystać z dedykowanych do tego funkcji.
Zapoznać się z: https://docs.python.org/3/library/time.html#time.perf_counter oraz zbadaj,
jak zmienia się czas skalowania obrazu w zależności od użytej interpolacji.
'''
import time

import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import perf_counter, perf_counter_ns

img = cv2.imread('Zdj_1.jpg') # Wczytanie zdjęcia

t_start = time.perf_counter()
img_scaled_linear = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR) # Przeskalowanie obrazu
t_stop = time.perf_counter()
print(f'Linear: {t_stop - t_start} s')

t_start = time.perf_counter()
img_scaled_inter_nearest = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST) # Przeskalowanie obrazu
t_stop = time.perf_counter()
print(f'Nearest: {t_stop - t_start} s')

t_start = time.perf_counter()
img_scaled_area = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA) # Przeskalowanie obrazu
t_stop = time.perf_counter()
print(f'Area: {t_stop - t_start} s')

t_start = time.perf_counter()
img_scaled_lanczos = cv2.resize(img, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4) # Przeskalowanie obrazu
t_stop = time.perf_counter()
print(f'Lanczos: {t_stop - t_start} s')
