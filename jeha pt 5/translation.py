import numpy as np
import os
import imutils
import cv2

img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))


M = np.float32([[1, 0, -50], [0, 1, -25]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("Shifted Down and Right", shifted)
cv2.imshow("Shifted Up and Left", shifted)  
cv2.waitKey(50000)