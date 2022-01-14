# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:21:54 2020

@author: luisc
"""

import cv2

fileDir = "Database/"
fileName = "JonquilFlowers.jpg"

img = cv2.imread(fileDir+fileName)
imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Image',img)

thres,bw = cv2.threshold(imgg,140,255,cv2.THRESH_BINARY)

cv2.imshow('BW Image',bw)

strElem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11),(-1,-1))

#bw1 = cv2.dilate(bw,strElem)
#bw2 = cv2.erode/bw,strElem)
bw1 = cv2.morphologyEx(img,cv2.MORPH_CLOSE,strElem)
bw2 = cv2.morphologyEx(img,cv2.MORPH_OPEN,strElem)

cv2.imshow('BW Morph Image 1',bw1)
cv2.imshow('BW Morph Image 2',bw2)

cv2.waitKey(0)
cv2.destroyAllWindows()

