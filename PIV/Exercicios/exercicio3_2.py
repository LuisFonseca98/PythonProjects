# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:16:35 2020

@author: luisc
"""

import cv2
import numpy as np

fileDir = "Database/"
objFileName = "falcon.jpg"
bgFileName = "florest.jpg"

chromaKey_Color = np.array([101,236,192])

objImage = cv2.imread(fileDir+objFileName)
bgImage = cv2.imread(fileDir+bgFileName)


maskImageInv = cv2.inRange(objImage,chromaKey_Color-20,chromaKey_Color+20)
maskImageM = 255-maskImageInv

cv2.imshow('Mask Original',maskImageM)

kernell = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11),(-1,-1))
maskImageMM = cv2.morphologyEx(maskImageM,cv2.MORPH_OPEN,kernell)

kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5),(-1,-1))
maskImageMM2 = cv2.erode(maskImageMM,kernel2)

cv2.imshow('Mask',maskImageMM2)

maskImage = cv2.cvtColor(maskImageMM2,cv2.COLOR_GRAY2BGR)

img1 = cv2.multiply(objImage,maskImage,scale=1.0/255)
img2 = cv2.multiply(bgImage,255-maskImage,scale=1.0/255)

outImage = cv2.add(img1,img2)

#blurEffect = cv2.blur(outImage,(5,5))
#gaussianBlueEffect = cv2.GaussianBlur(outImage,(5,5),0)
medianBlur = cv2.medianBlur(outImage,5)
cv2.imshow('Image Out',outImage)
cv2.imshow('Image Part 1',img1)
cv2.imshow('Image Part 2',img2)
#cv2.imshow('Image Blur',blurEffect)
#cv2.imshow('Image Gaussian Blur',gaussianBlueEffect)
cv2.imshow('Image Blur',medianBlur)
cv2.waitKey(0)

cv2.destroyAllWindows()
