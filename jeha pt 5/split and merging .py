import numpy as np
import cv2
import os

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg") 
img = cv2.imread(img_path)
(B, G, R) = cv2.split(img)

cv2.imshow("Red Channel", R)
cv2.imshow("Green Channel", G)
cv2.imshow("Blue Channel", B)
merged = cv2.merge([B, G, R])
#cv2.imshow("Merged Image", merged)
# cv2.waitKey(50000)
# cv2.destroyAllWindows()

zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))   
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(50000)