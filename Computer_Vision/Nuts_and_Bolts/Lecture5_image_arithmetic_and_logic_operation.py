#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
img11 = cv2.imread('mimg1.png')
img22 = cv2.imread('mimg2.png')
img3 = cv2.imread('mimg3.jpeg')

img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 235, 255, cv2.THRESH_BINARY_INV)

rows,cols,channels = img3.shape

roi = img11[0:rows, 0:cols ]


mask_inv = cv2.bitwise_not(mask)

cv2.imshow('img2gray', img2gray)

cv2.imshow('mask', mask)

cv2.imshow('mask_inv', mask_inv)

cv2.imshow('img11', img11)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img3_fg = cv2.bitwise_and(img3,img3,mask = mask)

cv2.imshow('img3_fg', img3_fg)
cv2.imshow('img3', img3)

dst = cv2.add(img1_bg,img3_fg)
img11[0:rows, 0:cols ] = dst

cv2.imshow('res',img11)

cv2.imshow('roi', roi)
cv2.imshow('dst', dst)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)


cv2.waitKey(1)
k = cv2.waitKey(0)
cv2.destroyAllWindows()