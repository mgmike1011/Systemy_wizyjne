'''

'''
import cv2
import numpy as np
img = img = cv2.imread('not_bad.jpg')
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_grey = img
cv2.namedWindow('Image')
th1 = 52
kernel = np.ones((5, 5), np.uint8)

ret, thresh1 = cv2.threshold(img_grey, th1, 255, cv2.THRESH_BINARY)
thresh1 = cv2.dilate(thresh1, kernel, iterations=1)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1:5]
cv2.drawContours(img, cnt, -1, (255, 255, 0), thickness=2, lineType=cv2.LINE_AA)
'''
4 3
2 1
'''
ar = []
for i in cnt:
    M = cv2.moments(i)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    area = cv2.contourArea(i)
    ar.append([cx, cy])

# Wyprostowanie obrazu:
dest = np.float32([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
M = cv2.getPerspectiveTransform(np.float32([ar[3], ar[2], ar[0], ar[1]]), dest)
img = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(10) == ord('q'):
        break
