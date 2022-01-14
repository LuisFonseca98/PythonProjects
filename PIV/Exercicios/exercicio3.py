# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:01:51 2020

@author: luisc
"""

import cv2
import numpy as np

fileDir = "Database/"
objFileName = "falcon.jpg"
bgFileName = "florest.jpg"
maskFileName = "mask.png"


objImage = cv2.imread(fileDir+objFileName)
bgImage = cv2.imread(fileDir+bgFileName)
maskImage = cv2.imread(fileDir+maskFileName)

img1 = cv2.multiply(objImage,maskImage,scale=1.0/255)
img2 = cv2.multiply(bgImage,255-maskImage,scale=1.0/255)

outImage = cv2.add(img1,img2)


cv2.imshow('Image Out',outImage)
cv2.imshow('Image Part 1',img1)
cv2.imshow('Image Part 2',img2)
cv2.waitKey(0)

cv2.destroyAllWindows()


