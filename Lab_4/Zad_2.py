'''
Napisz program rysujący kwadrat po naciśnięciu lewego klawisza myszy oraz okrąg po naciśnięciu prawego.
Wykorzystaj do tego celu funkcję cv2.circle oraz cv2.rectangle (dokumentacja),
wykorzystując do tego celu współrzędne kursora myszy i przykładowy kod dostępny w https://docs.opencv.org/5.x/db/d5b/tutorial_py_mouse_handling.html.
'''
import cv2
import numpy as np


img = cv2.imread('road.jpg') # Wczytanie zdjęcia
img = cv2.resize(img,(0, 0), fx=0.5, fy=0.5)

points = []

def mouse_call(event,x,y,flags,param):
    global points, img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
    if len(points) == 4:
        dest = np.float32([[0, 0], [img.shape[0], 0], [img.shape[0], img.shape[1]], [0, img.shape[1]]]) #moga byc 200 x 900
        M = cv2.getPerspectiveTransform(np.float32(points), dest)
        img = cv2.warpPerspective(img, M, (img.shape[0], img.shape[1]))
        points = []
        '''
        kolejnosc punktow
        1 2
        4 3
        '''


cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_call)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(10) == ord('q'):
        break