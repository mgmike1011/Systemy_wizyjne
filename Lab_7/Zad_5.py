'''
Prosty system automatycznej detekcji ruchu
Do jednego z zaimplementowanych algorytmów dodać moduł, który zlicza ile pikseli zostało uznanych za
zmienione i decyduje, na tej podstawie, o uruchomieniu alarmu (np. zapisaniu danej klatki obrazu w celu jej
analizy przez operatora).
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

backSub = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
fgMask = backSub.apply(frame)
last_frame = fgMask.copy()
while True:
    ret, frame = cap.read()
    fgMask = backSub.apply(frame)
    x, c = np.unique([e1 != e2 for e1, e2 in zip(last_frame, fgMask)], return_counts=True)
    # print(c[1])
    if c[1] > 2000:
        print("Alarm")

    last_frame = fgMask.copy()
    cv2.imshow('FG Mask', fgMask)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
