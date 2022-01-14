from exercicio1 import DCT, IDCT
from exercicio2 import Quantificacao, Desquantificacao, SNR
from exercicio3 import codificadorDC, descodificadorDC
from exercicio4 import codificadorAC, descodificadorAC
from exercicio5 import DCAC, inv_zigzag
from exercicio6 import write2File
from exercicio7 import readFile
import cv2
from tabelas import Q, K3, K5
import numpy as np
import os
import matplotlib.pyplot as plt
from time import time


def compressionRate(img1name, img2name):
    
    sizeO = os.path.getsize(img1name)
    sizeA = os.path.getsize(img2name)
    taxaCompressao = sizeO/sizeA
    
    return taxaCompressao

def ex8910():
    

    img = cv2.imread("LenaGray.tif", cv2.IMREAD_GRAYSCALE)
    img_20 = np.array(img, dtype = np.float64)
    bloco_width = 8
    bloco_height = 8
    
    altura, largura = img_20.shape
    altura = altura / bloco_height
    largura = largura / bloco_width
    
    
    fatores_qualidade = [25, 50, 75]
    snr_arr = []
    taxas_comp = []
    tempos_compressao = []
    tempos_descompressao = []
    
    print("EXERCICIO 8")
    print("-------------------------------------------------------------------")
    
    for i in range(len(fatores_qualidade)):

        filename = "lena_ex8_"+str(fatores_qualidade[i])+".txt"
        dct = DCT(img_20)
        quantificacao = Quantificacao(dct, Q, fatores_qualidade[i])
        
        t0 = time()
    
        codDC = codificadorDC(quantificacao, K3)
        codAC = codificadorAC(quantificacao, K5)
        
        tc = time() -t0
        
        write2File(codAC, codDC, filename)
        ACfromFile, DCfromFile = readFile(filename)
        
        t0 = time()
        
        descDC= descodificadorDC(DCfromFile, K3, altura, largura)
        descAC = descodificadorAC(ACfromFile, K5, altura, largura)
        
        td = time() -t0
                
        #SERVE PARA CONVERTER O MODO ZIG ZAG EM ORIGINAL
        inverso_acs = inv_zigzag(descAC)          
        acsdcs = DCAC(descDC, inverso_acs)
        
        desquantificacao = Desquantificacao(acsdcs, Q, fatores_qualidade[i])
        idct = IDCT(desquantificacao, img_20)
        
        snr = SNR(img,idct)
        print('SNR ' + str(fatores_qualidade[i])+ ':', snr)
        
        cv2.imwrite("Lena_ex8_" + str(fatores_qualidade[i]) + ".jpg", idct)
        
        taxa_compressao = compressionRate("LenaGray.tif", "Lena_ex8_" + str(fatores_qualidade[i]) + ".jpg")
        print("TAXA COMPRESSÃO:"+str(fatores_qualidade[i]) + ":", taxa_compressao)
        
        print("TEMPO DE COMPRESSAO:", tc)
        print("TEMPO DE DESCOMPRESSÃO:", td)
        print("-------------------------------------------------------------------")
        
        snr_arr.append(snr)
        taxas_comp.append(taxa_compressao)
        tempos_compressao.append(tc)
        tempos_descompressao.append(td)
      
    # Grafico SNR / Taxa    
    plt.title("Taxa de compressao em funcao da SNR: ")
    plt.plot(snr_arr, taxas_comp, 'g')
    plt.xlabel('SNR')
    plt.ylabel('Taxa de Compressao')
    plt.grid(color='r', linestyle='-', linewidth=0.5)
    plt.show()
    
    # Grafico SNR / Qualidade
    plt.plot(snr_arr, fatores_qualidade)
    plt.xlabel('SNR')
    plt.ylabel("Qualidade")
    plt.grid(color='r', linestyle='-', linewidth=0.5)
    plt.show()
    
    # Grafico Taxa / Qualidade
    plt.plot(taxas_comp, fatores_qualidade)
    plt.xlabel('Taxa de Compressao')
    plt.ylabel("Qualidade")
    plt.grid(color='r', linestyle='-', linewidth=0.5)
    plt.show()
    
        
if __name__ == '__main__':
    
    ex8910()
    
