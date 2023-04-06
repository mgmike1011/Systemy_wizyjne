'''
Pobierz dwa obrazy z wprowadzonymi zakłóceniami:
    lenna_noise.bmp
    lenna_salt_and_pepper.bmp
Wyświetl jeden z pobranych obrazów, a następnie korzystając z poznanych funkcji do filtracji (filtr uśredniający, filtr Gaussa, filtr medianowy)
    zaprezentuj ich działanie. Wyświetlić rezultat działania każdego z filtrów w osobnym oknie w celu porównania efektów filtracji.
Dodaj trackbar umożliwiający sterowanie rozmiarem okna filtracji (wartość powinna być nieparzysta, wykorzystaj wzór na liczby nieparzyste 2n+1).
Wykonaj filtrację na obu obrazach z zakłóceniami. Zwróć uwagę na efekty filtracji: w zależności od naniesionego szumu oraz rozmiaru okna filtracji.
'''
import cv2

img_1 = cv2.imread('lenna_noise.bmp')
img_2 = cv2.imread('lenna_salt_and_pepper.bmp')


def window_callback(value):
    global window
    window = 2*value + 1


window = 5
cv2.namedWindow('Window')
cv2.createTrackbar('alpha', 'Window', 0, 100, window_callback)
while True:
    img_1_blur = cv2.blur(img_1, (window, window))
    img_1_gauss = cv2.GaussianBlur(img_1, (window, window), 0)
    img_1_median = cv2.medianBlur(img_1, window)

    cv2.imshow('Blur', img_1_blur)
    cv2.imshow('Gaussian', img_1_gauss)
    cv2.imshow('Median', img_1_median)

    img_2_blur = cv2.blur(img_2, (window, window))
    img_2_gauss = cv2.GaussianBlur(img_2, (window, window), 0)
    img_2_median = cv2.medianBlur(img_2, window)

    cv2.imshow('Blur_2', img_2_blur)
    cv2.imshow('Gaussian_2', img_2_gauss)
    cv2.imshow('Median_2', img_2_median)

    if cv2.waitKey(10) == ord('q'):
        break