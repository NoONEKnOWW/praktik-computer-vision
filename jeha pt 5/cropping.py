import numpy as np
import os
import cv2

# Load the image
img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

cropped = img[50:200, 200:400]
cv2.imshow("Original", img)
cv2.imshow("Cropped", cropped)
cv2.waitKey(50000)