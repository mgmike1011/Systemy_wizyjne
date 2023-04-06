'''
Napisz program rysujący kwadrat po naciśnięciu lewego klawisza myszy oraz okrąg po naciśnięciu prawego.
Wykorzystaj do tego celu funkcję cv2.circle oraz cv2.rectangle (dokumentacja),
wykorzystując do tego celu współrzędne kursora myszy i przykładowy kod dostępny w https://docs.opencv.org/5.x/db/d5b/tutorial_py_mouse_handling.html.
'''
import cv2
import numpy as np


# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x,y),(x+10,y+10),(0,255,0),-1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()