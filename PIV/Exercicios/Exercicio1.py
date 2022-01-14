import cv2
import numpy as np
from PIL import Image

#EXERCICIO 1.1
im = cv2.imread('Database/lena.png')
#Display the image
# =============================================================================
# cv2.imshow('im1',im)
# cv2.imshow('im2',im[:,:,0])
# cv2.imshow('im3',im[:,:,1])
# cv2.imshow('im4',im[:,:,2])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

#EXERCICIO1.2
cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

#EXERCICIO1.3
# im = Image.open("lena.png")
# width,height = im.size
# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5
# im1 = im.crop((left,top,right,bottom))
# newSize = (300,300)
# im1 = im1.resize(newSize)
# im1.show()