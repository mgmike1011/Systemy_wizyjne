'''
Napisz funkcję implementującą filtr Kuwahary (do obliczeń dla wygody wykorzystać można funkcję meanStdDev).
'''
import cv2
import numpy as np

img = cv2.imread('lenna_noise.bmp')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # konwersja do skali szarości

for i in range(img_grey.shape[0]):
    for j in range(img_grey.shape[1]):
        if j % 3 == 0:
            img_grey[i, j] = 255


def kuwahara_filter(img):
    l = 2
    img_out = np.zeros(img.shape, dtype=np.uint8)
    for col in range(l + 1, img.shape[0] - (l + 1)):
        for row in range(l + 1, img.shape[1] - (l + 1)):
            reg1_mean, reg1_dev = cv2.meanStdDev(np.array(
                [img[row - 2, col - 2], img[row - 2, col - 1], img[row - 2, col],
                 img[row - 1, col - 2], img[row - 1, col - 1], img[row - 1, col],
                 img[row, col - 2], img[row, col - 1], img[row, col]]))
            reg2_mean, reg2_dev = cv2.meanStdDev(np.array(
                [img[row - 2, col], img[row - 2, col + 1], img[row - 2, col + 2],
                 img[row - 1, col], img[row - 1, col + 1], img[row - 1, col + 2],
                 img[row, col], img[row, col + 1], img[row, col + 2]]))
            reg3_mean, reg3_dev = cv2.meanStdDev(
                np.array([img[row, col], img[row, col + 1], img[row, col + 2],
                          img[row + 1, col], img[row + 1, col + 1], img[row + 1, col + 2],
                          img[row + 2, col], img[row + 2, col + 1], img[row + 2, col + 2]]))
            reg4_mean, reg4_dev = cv2.meanStdDev(np.array(
                [img[row, col - 2], img[row, col - 1], img[row + 1, col - 2],
                 img[row + 1, col - 1], img[row + 1, col - 2], img[row + 1, col],
                 img[row + 2, col], img[row + 2, col - 1], img[row + 2, col - 2]]))
            mean = [reg1_mean, reg2_mean, reg3_mean, reg4_mean]
            dev = [reg1_dev, reg2_dev, reg3_dev, reg4_dev]
            min_ = min(dev)
            min_i = dev.index(min_)
            val = mean[min_i][0][0]
            img_out[row, col] = val
    return img_out


img_filter = kuwahara_filter(img_grey)
cv2.imshow('Filter', img_filter)
key = cv2.waitKey(0)
