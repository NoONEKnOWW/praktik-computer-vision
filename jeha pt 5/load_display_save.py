from __future__ import print_function
import cv2
import os

# buka gambar
img_path = os.path.join(".", "img/colorbar.jpeg")
img = cv2.imread(img_path)
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

cv2.imshow("Image", img)
cv2.waitKey(50000)
cv2.imwrite("output/colorbar_output.jpg", img)