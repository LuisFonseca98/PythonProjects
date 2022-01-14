
import numpy as np
import cv2

def DCT(img):
    tam = img.shape
    array_final = np.array(img)
    
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = img[i:i+8,j:j+8]
            bloco_dct = cv2.dct(bloco)
            array_final[i:i+8,j:j+8] = bloco_dct     
    return array_final
    
def IDCT(dct, img):
    tam = img.shape
    array_final = np.array(img)
    
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = dct[i: i+8,j:j+8]
            inversa = cv2.dct(bloco,np.array(bloco),cv2.DCT_INVERSE)
            array_final[i:i+8,j:j+8] = inversa
    return array_final


def ex1(img):
    dct = DCT(img)
    idct = IDCT(dct, img)
    cv2.imwrite("dct.tif", dct)
    cv2.imwrite("idct.tif", idct)
    
    
if __name__ == '__main__':
    
    img_1 = cv2.imread("LenaGray.tif", cv2.IMREAD_GRAYSCALE)
    img_20 = np.array(img_1, dtype = np.float64)
    ex1(img_20)
    