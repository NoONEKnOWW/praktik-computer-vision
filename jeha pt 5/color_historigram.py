from __future__ import print_function
from matplotlib import pyplot as plt
import cv2
import os
import numpy as np

# buka gambar
img_path = os.path.join(".", "img/colorbar.jpeg")    
img = cv2.imread(img_path)
cv2.imshow("Original", img)

chans = cv2.split(img)
colors = ("b", "g", "r")    
plt.figure()
plt.title("'Color Histogram'")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")   
features = []
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    features.extend(hist)
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1],chans [0]], [0, 1], None, 
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
fig.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans [2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
fig.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0],chans [2]],[0, 1], None, 
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
fig.colorbar(p)

print ("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0])
)

hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], 
                    [0, 256, 0, 256, 0, 256])
print ("3D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0])
)
plt.show()