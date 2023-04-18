'''

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

img = cv2.imread('detekcja_deskrypcja_dopasowanie/forward-1.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwersja do skali szarości

for i in range(1, 7):
    img = cv2.imread(f'detekcja_deskrypcja_dopasowanie/forward-{i}.bmp')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # konwersja do skali szarości

    print(f'################ forward-{i}.bmp ################ ')
    print(f'////////// FAST /////////// ')
    # FAST
    fast = cv2.FastFeatureDetector_create()  # inicjalizacja detektora
    t_start = time.perf_counter()
    kp = fast.detect(img, None)  # detekcja
    t_stop = time.perf_counter()
    print(f'FAST: {t_stop - t_start} s')
    img1 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))  # narysowanie wykrytych punktów
    # Wyświetlenie danych
    print("Threshold: {}".format(fast.getThreshold()))
    print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
    print("neighborhood: {}".format(fast.getType()))
    print("Total FAST Keypoints with nonmaxSuppression: {}".format(len(kp)))

    print(f'////////// ORB /////////// ')
    # ORB
    orb = cv2.ORB_create()  # inicjalizacja detektora
    t_start = time.perf_counter()
    kp = orb.detect(img, None)  # znalezienie punktów kluczowych
    # kp, des = orb.compute(img, kp)  # Deskrypcja
    t_stop = time.perf_counter()
    print(f'ORB: {t_stop - t_start} s')
    img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)  # narysowanie wykrytych punktów
    print("Total ORB Keypoints : {}".format(len(kp)))

    print(f'////////// SIFT /////////// ')
    # SIFT
    sift = cv2.SIFT_create()
    t_start = time.perf_counter()
    kp = sift.detect(img, None)
    t_stop = time.perf_counter()
    print(f'SIFT: {t_stop - t_start} s')
    img3 = cv2.drawKeypoints(img, kp, img)
    print("Total SIFT Keypoints : {}".format(len(kp)))
    print('')

#     Parametry w algorytmach
#     nonmaxSuppression w FAST -

while True:
    cv2.imshow('Image FAST', img1)
    cv2.imshow('Image ORB', img2)
    cv2.imshow('Image SIFT', img3)
    if cv2.waitKey(10) == ord('q'):
        break