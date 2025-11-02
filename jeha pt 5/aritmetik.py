import cv2
import numpy as np
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

(hight, width) = img.shape[:2]
center = (width // 1080, hight // 720)

m = np.ones(img.shape, dtype="uint8") * 75
added = cv2.add(img, m)
subtracted = cv2.subtract(img, m)

cv2.imshow("Added", added)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(50000)