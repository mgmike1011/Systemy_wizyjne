'''
Bazując na: https://docs.opencv.org/5.x/d0/d86/tutorial_py_image_arithmetics.html, napisz funkcję wyznaczającą negatyw obrazu.
'''
import cv2


def negative_image(img):
    neg_img = cv2.bitwise_not(img)
    return neg_img


img = cv2.imread('Zdj_1.jpg') #Wczytanie zdjęcia

neg_ing = negative_image(img)
cv2.imshow('Adaptive Gaussian', neg_ing)

while True:
    if cv2.waitKey(10) == ord('q'):
        break