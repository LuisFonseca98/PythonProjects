import cv2
import numpy as np
import matplotlib.pyplot as plt


fileDir = "Database/"
fileName = "fingerprint.jpg"
fileName2 = "fingerprintS.jpg"

img = cv2.imread(fileDir + fileName)

cv2.imshow('Image',img)

Ifx = .2
Ify = .2

img2 = cv2.resize(img,None,fx = Ifx,fy = Ify,interpolation = cv2.INTER_NEAREST)

cv2.imshow('Image2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

