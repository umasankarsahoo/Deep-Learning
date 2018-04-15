import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('bookpage.jpg')

cv2.imshow('img1.jpg',img1)


retval , threshold = cv2.threshold(img1,10,255,cv2.THRESH_BINARY)

cv2.imshow('threshold',threshold)

gray =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
retval1 , threshold1 = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

cv2.imshow('gray',threshold1)

th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive threshold',th)


retval2,threshold2 = cv2.threshold(gray,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold2)


cv2.waitKey(0)
cv2.destroyAllWindows()