import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), dtype=np.uint8)
center = (250, 250)
color_silver = (200, 200, 200)


cv2.circle(canvas, center, 200, color_silver, 10)


cv2.line(canvas, center, (250, 60), color_silver, 10)
cv2.line(canvas, center, (80, 340), color_silver, 10)
cv2.line(canvas, center, (420, 340), color_silver, 10)

cv2.imwrite("ikan.jpg", canvas)

print("Gambar logo Mercedes telah disimpan sebagai karakter.png")
