from __future__ import print_function
import os
import cv2
import numpy as np

img_path = os.path.join(".", "img/colorbar.jpeg") 
img = cv2.imread(img_path)

(b, g, r) =img[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

img[0, 0] = (0, 0, 255)
(b, g, r) = img[0, 0]
print("Modified Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
corner = img[0:100, 0:100]
img[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Modified", img)
cv2.imshow("Corner", corner)
cv2.waitKey(50000)
