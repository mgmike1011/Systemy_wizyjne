'''

'''
import cv2
import numpy as np

img = cv2.imread('Mops.jpg')
# img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rec = cv2.imread('face.png')

template = cv2.cvtColor(img_rec, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

while True:
    cv2.imshow('IMG_res', res)
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break
