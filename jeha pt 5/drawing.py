import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)


titik_tengah = (250, 250)
radius = 50 
red = (0, 0, 255)
thickness = 2
cv2.circle(canvas, titik_tengah, radius, red, thickness)

cv2.imshow("Canvas", canvas)
cv2.waitKey(5000)