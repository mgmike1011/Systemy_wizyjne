'''
Napisaz program, który po wskazaniu przez użytkownika czterech punktów na obrazie docelowym wklei w niego drugi obraz tak,
 aby wskazane punkty określały jego narożniki (celem jest zastąpienie jednego z obrazów wiszących w galerii sztuki obrazem mopsa).
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gallery.png') # Wczytanie zdjęcia
pug = cv2.imread('Mops.jpg')

positions = []
pointIndex = 0

def mouse_call(event,x,y,flags,param):
    global img, pug
    global positions
    global pointIndex
    if event == cv2.EVENT_LBUTTONDOWN:
        positions.append([x, y])
    if len(positions) == 4:
        height, width, channels = img.shape
        h1_p, w1_p, ch1_p = pug.shape
        pts1 = np.float32([[0, 0], [w1_p, 0], [0, h1_p], [w1_p, h1_p]])
        pts2 = np.float32(positions)
        h, mask_h = cv2.findHomography(pts1, pts2)
        im1Reg = cv2.warpPerspective(pug, h, (width, height))
        mask2 = np.zeros(img.shape, dtype=np.uint8)
        roi_corners2 = np.int32([positions[0], positions[1], positions[3], positions[2]])
        cv2.fillConvexPoly(mask2, roi_corners2, (255,) * channels)
        mask2 = cv2.bitwise_not(mask2)
        masked_image2 = cv2.bitwise_and(img, mask2)
        img = cv2.bitwise_or(im1Reg, masked_image2)
        positions = []
        pointIndex = 0
        '''
        kolejnosc punktow
        1 2
        3 4
        '''
        '''
        https://medium.com/acmvit/how-to-project-an-image-in-perspective-view-of-a-background-image-opencv-python-d101bdf966bc
        '''


cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_call)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
