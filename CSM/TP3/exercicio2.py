
import numpy as np
import cv2
from tabelas import Q,quality_factor
from exercicio1 import DCT, IDCT


def SNR(original,descodificada):
    imageO = original.ravel()
    noise = original.astype(float) - descodificada.astype(float)
    imageA = noise.ravel()

    pOriginal = np.sum(imageO**2.)
    pdescodificada = np.sum(imageA**2.)
    SNR = 10*np.log10(pOriginal/pdescodificada)

    return round(SNR,2)


def Quantificacao(dct,Q,per):
    tam = dct.shape
    array_final = np.array(dct)
    fator_compressao = np.multiply(Q,quality_factor(per))
    
    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco_dct = dct[i:i+8,j:j+8]
            quantificacao = np.round(np.divide(bloco_dct, fator_compressao))
            array_final[i:i+8,j:j+8] = quantificacao     
    return array_final
    
def Desquantificacao(quant,Q,per):
    tam = quant.shape
    array_final = np.array(quant)
    fator_compressao = np.multiply(Q,quality_factor(per))

    for i in np.arange(0,tam[0],8): 
        for j in np.arange(0,tam[1],8):
            bloco = quant[i: i+8,j:j+8]
            desquant = np.round(np.multiply(bloco, fator_compressao))
            array_final[i:i+8,j:j+8] = desquant
    return array_final


def ex2(img):
    print("EXERCICIO 2")
    
    fator_qualidade = 25
    
    dct = DCT(img_20)
    quant = Quantificacao(dct,Q,fator_qualidade)
    desquant = Desquantificacao(quant,Q,fator_qualidade)
    idct = IDCT(desquant, img_20)
    
    print('SNR ' + str(fator_qualidade)+ ':', SNR(img,idct))
    cv2.imwrite("DCT_" + str(fator_qualidade) + ".tif", quant)
    cv2.imwrite("IDCT_" + str(fator_qualidade) + ".tif", idct)
    
    fator_qualidade = 50
    
    dct = DCT(img_20)
    quant = Quantificacao(dct,Q,fator_qualidade)
    desquant = Desquantificacao(quant,Q,fator_qualidade)
    idct = IDCT(desquant, img_20)
    
    print('SNR ' + str(fator_qualidade)+ ':', SNR(img,idct))
    cv2.imwrite("DCT_" + str(fator_qualidade) + ".tif", quant)
    cv2.imwrite("IDCT_" + str(fator_qualidade) + ".tif", idct)
    
    fator_qualidade = 75
    
    dct = DCT(img_20)
    quant = Quantificacao(dct,Q,fator_qualidade)
    desquant = Desquantificacao(quant,Q,fator_qualidade)
    idct = IDCT(desquant, img_20)
    
    print('SNR ' + str(fator_qualidade)+ ':', SNR(img,idct))
    cv2.imwrite("DCT_" + str(fator_qualidade) + ".tif", quant)
    cv2.imwrite("IDCT_" + str(fator_qualidade) + ".tif", idct)
    
    print("-------------------------------------------------------------------")
    
if __name__ == '__main__':
    
    img_1 = cv2.imread("LenaGray.tif", cv2.IMREAD_GRAYSCALE)
    img_20 = np.array(img_1, dtype = np.float64)
    
    ex2(img_20)
    
