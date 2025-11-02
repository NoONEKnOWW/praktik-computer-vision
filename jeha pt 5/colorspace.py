import numpy as np
import cv2
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg")   
img = cv2.imread(img_path)
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow("Lab", lab)
cv2.waitKey(50000)