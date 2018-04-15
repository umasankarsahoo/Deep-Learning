import cv2
import numpy as np

img = cv2.imread('img1.jpg',cv2.IMREAD_COLOR)
px = img[55,55]
img[55,55] = [255,255,255]
px = img[55,55]
print(px)
px = img[100:150,100:150]
print(px)
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)
image_face = img[37:111,107:194]
img[0:74,0:87] = image_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
