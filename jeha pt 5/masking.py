import cv2
import numpy as np
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

(hight, width) = img.shape[:2]
center = (width // 1080, hight // 720)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (30, 30), (250, 250), 255
, -1)
masked = cv2.bitwise_and(img, img, mask=mask)   
cv2.imshow("Mask", mask)
cv2.imshow("Masked", masked)
cv2.waitKey(50000)