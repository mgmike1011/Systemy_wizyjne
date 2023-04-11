'''
Zmodyfikować program z punktu 1, aby zapamiętywał trzy kolejne klatki obrazu (nazwać je previous_frame (),
current_frame () oraz next_frame()).
Wyznaczyć bezwzględną różnicę między obrazem next_frame oraz current_frame, a także między next_frame oraz previous_frame.
Wykonać operację bitową AND (cv2.bitwise_and) pomiędzy obrazami różnicowymi uzyskanymi w poprzednim kroku.
Dodać operację domknięcia, a następnie progowania (jak w punkcie 1).
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
previous_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, frame = cap.read()
current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, frame = cap.read()
next_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while True:
    diff_1 = cv2.absdiff(current_frame, next_frame)
    diff_2 = cv2.absdiff(next_frame, previous_frame)
    diff = cv2.bitwise_and(diff_1, diff_2)
    diff = cv2.morphologyEx(diff, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    _, diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

    previous_frame = current_frame
    current_frame = next_frame
    ret, frame = cap.read()
    next_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Frame diff", diff)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
