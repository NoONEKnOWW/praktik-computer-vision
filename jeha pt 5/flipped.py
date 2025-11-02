import cv2
import numpy as np
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

(hight, width) = img.shape[:2]
center = (width // 1080, hight // 720)

f = cv2.flip(img, 1)    
cv2.imshow("Flipped", f)
cv2.waitKey(50000)  
  