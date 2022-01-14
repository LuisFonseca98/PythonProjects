from exercicio1 import DCT, IDCT
from exercicio2 import Quantificacao, Desquantificacao
from exercicio3 import codificadorDC, descodificadorDC
from exercicio4 import codificadorAC, descodificadorAC
import cv2
from tabelas import Q, K3, K5, zigzag
import numpy as np


def DCAC(codDC, codAC):
    tam = codAC.shape
    x = 0
    
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8): 
            bloco = codAC[lin:lin+8,col:col+8]
            bloco[0][0] = codDC[x]
            codAC[lin:lin+8,col:col+8] = bloco
            x += 1
    
    return codAC
    

''' Métodos auxiliares '''
def inv_zigzag(matriz):
    ind_O = zigzag.reshape((64),order='F').astype('int')
    
    tam = matriz.shape
    blocos = np.array(matriz)
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8):  
            bloco = matriz[lin:lin+8,col:col+8].flatten()
            bloco_zz = bloco[ind_O].reshape((8,8),order='F')
            blocos[lin:lin+8,col:col+8] = bloco_zz
    return blocos

def ex5():
    

    img = cv2.imread("LenaGray.tif", cv2.IMREAD_GRAYSCALE)
    img_20 = np.array(img, dtype = np.float64)
    bloco_width = 8
    bloco_height = 8
    
    altura, largura = img_20.shape
    altura = altura / bloco_height
    largura = largura / bloco_width
    
    
    fatores_qualidade = [25, 50, 75]
    
    for i in range(len(fatores_qualidade)):
        
        dctPic = DCT(img_20)
        dctQuantificado = Quantificacao(dctPic, Q, fatores_qualidade[i])
        codDC = codificadorDC(dctQuantificado, K3)
        codAC = codificadorAC(dctQuantificado, K5)
        
        descDC= descodificadorDC(codDC, K3, altura, largura)
        
        descAC = descodificadorAC(codAC, K5, altura, largura)
                
        #SERVE PARA CONVERTER O MODO ZIG ZAG EM ORIGINAL
        inverso_acs = inv_zigzag(descAC)
                
        acsdcs = DCAC(descDC, inverso_acs)
        
        desquantificacao = Desquantificacao(acsdcs, Q, fatores_qualidade[i])
        idct = IDCT(desquantificacao, img_20)
        
        cv2.imwrite("Lena_ex5_" + str(fatores_qualidade[i]) + ".tif", idct)
        
        
if __name__ == '__main__':
    
    ex5()
    
