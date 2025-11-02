import cv2
import numpy as np

image = cv2.imread('colorbar.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)