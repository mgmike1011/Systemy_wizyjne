import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

img1 = cv2.imread(f'detekcja_deskrypcja_dopasowanie/rotate-1.bmp')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # konwersja do skali szarości

img2 = cv2.imread(f'detekcja_deskrypcja_dopasowanie/rotate-6.bmp')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # konwersja do skali szarości

# ////////////////////// Detekcja ////////////////////
# ////// img1
# FAST
fast = cv2.FastFeatureDetector_create()  # inicjalizacja detektora
kp1_fast = fast.detect(img1, None)  # detekcja
# img1 = cv2.drawKeypoints(img1, kp1_fast, None, color=(255, 0, 0))

# ORB
orb = cv2.ORB_create()  # inicjalizacja detektora
kp1_orb = orb.detect(img1, None)  # znalezienie punktów kluczowych
# img1 = cv2.drawKeypoints(img1, kp1_orb, None, color=(0, 255, 0), flags=0)  # narysowanie wykrytych punktów

# ////// img2
# FAST
fast = cv2.FastFeatureDetector_create()  # inicjalizacja detektora
kp2_fast = fast.detect(img2, None)  # detekcja
# img1 = cv2.drawKeypoints(img1, kp2_fast, None, color=(255, 0, 0))

# ORB
orb = cv2.ORB_create()  # inicjalizacja detektora
kp2_orb = orb.detect(img2, None)  # znalezienie punktów kluczowych
# img2 = cv2.drawKeypoints(img2, kp2_orb, None, color=(0, 255, 0), flags=0)  # narysowanie wykrytych punktów


# ////////////////////// Deskrypcja ////////////////////
# BRIEF
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
t_start = time.perf_counter()
kp1_brief, des1_brief = brief.compute(img1, kp1_fast)  # Deskrypcja zdjęcie 1 z detektora FAST
kp2_brief, des2_brief = brief.compute(img2, kp2_fast)  # Deskrypcja zdjęcie 2 z detektora FAST
t_stop = time.perf_counter()
print(f'BRIEF - czas deskrypcji: {t_stop - t_start} s')

# ORB
orb = cv2.ORB_create()
t_start = time.perf_counter()
kp1_orb, des1_orb = orb.compute(img1, kp1_orb)  # Deskrypcja zdjęcie 1 z detektora orb
kp2_orb, des2_orb = orb.compute(img2, kp2_orb)  # Deskrypcja zdjęcie 2 z detektora orb
t_stop = time.perf_counter()
print(f'ORB - czas deskrypcji: {t_stop - t_start} s')

# SIFT
sift = cv2.SIFT_create()
t_start = time.perf_counter()
kp1_sift, des1_sift = sift.compute(img1, kp1_fast)  # Deskrypcja zdjęcie 1 z detektora FAST
kp2_sift, des2_sift = sift.compute(img2, kp2_fast)  # Deskrypcja zdjęcie 2 z detektora FAST
t_stop = time.perf_counter()
print(f'SIFT - czas deskrypcji: {t_stop - t_start} s')

# ////////////////////// Dopasowanie ////////////////////
# BRIEF
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches_brief = bf.match(des1_brief, des2_brief)
matches = sorted(matches_brief, key=lambda x: x.distance)
matched_image_brief = cv2.drawMatches(img1, kp1_brief, img2, kp2_brief, matches[:50], None, flags=2)

# ORB
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches_orb = bf.match(des1_orb, des2_orb)
matches = sorted(matches_orb, key=lambda x: x.distance)
matched_image_orb = cv2.drawMatches(img1, kp1_orb, img2, kp2_orb, matches, None, flags=2)

# Wyświetlenie co zwraca match
for i in matches[:20]:
    print(i.imgIdx)

while True:
    cv2.imshow('Image BRIEF', matched_image_brief)
    cv2.imshow('Image ORB', matched_image_orb)
    if cv2.waitKey(10) == ord('q'):
        break