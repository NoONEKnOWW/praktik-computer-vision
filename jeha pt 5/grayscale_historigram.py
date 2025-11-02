from matplotlib import pyplot as plt
import cv2
import os

# buka gambar
img_path = os.path.join(".", "img/colorbar.jpeg")
img = cv2.imread(img_path)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(50000)
