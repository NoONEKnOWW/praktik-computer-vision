import numpy as np
import os
import cv2

#buka gambar
img_path = os.path.join(".","img/colorbar.jpeg")
img = cv2.imread(img_path)

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    cv2.imshow(title, image)
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        hist = hist.flatten()
        hist_img = np.zeros((300, 256, 3), dtype="uint8")
        cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
        for x in range(1, 256):
            cv2.line(hist_img, (x - 1, 300 - int(hist[x - 1])),
                     (x, 300 - int(hist[x])),
                     (255 if color == "b" else 0,
                      255 if color == "g" else 0,
                      255 if color == "r" else 0), 2)
        cv2.imshow(f"{title} - {color.upper()} Histogram", hist_img)

cv2.imshow("Original Image", img)
plot_histogram(img, "Original Image Histogram")
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (250, 250), 255, -1)
cv2.imshow("Mask", mask)

masked_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked Image", masked_img)
plot_histogram(img, "Masked Image Histogram", mask=mask)

cv2.waitKey(50000)