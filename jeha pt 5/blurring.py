import numpy as np
import cv2
import os


#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg") 
img = cv2.imread(img_path)
cv2.imshow("Original Image", img)

blurred = np.hstack([
    cv2.blur(img, (3, 3)),
    cv2.blur(img, (5, 5)),
    cv2.blur(img, (7, 7))
])
cv2.imshow(" Blurs", blurred)
gaussianblurred = np.hstack([
    cv2.GaussianBlur(img, (3, 3), 0),
    cv2.GaussianBlur(img, (5, 5), 0),
    cv2.GaussianBlur(img, (7, 7), 0)
])
cv2.imshow("Gaussian Blurs", gaussianblurred)

median = np.hstack([
    cv2.medianBlur(img, 3),
    cv2.medianBlur(img, 5),
    cv2.medianBlur(img, 7)
])  
cv2.imshow("Median Blurs", median)

bilateral = np.hstack([
    cv2.bilateralFilter(img, 5, 21, 21),
    cv2.bilateralFilter(img, 7, 31, 31),
    cv2.bilateralFilter(img, 9, 41, 41)
])  
cv2.imshow("Bilateral Blurs", bilateral)
cv2.waitKey(50000)