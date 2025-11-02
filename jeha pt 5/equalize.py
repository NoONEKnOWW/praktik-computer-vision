import numpy as np
import cv2
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg") 
img = cv2.imread(img_path)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eq_img = cv2.equalizeHist(img)

cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", eq_img)
cv2.waitKey(5000)