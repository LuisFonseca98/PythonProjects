# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:17:18 2020

@author: Rodrigo
"""

import numpy as np
from tabelas import zigzag
from exercicio3 import Complemento

def codificadorAC(quant, K5):
    final = []
    tam = quant.shape

    #Ordenar o array zigzag pelos índices a percorrer
    zigzagOrdered = zigzag.reshape(64,order='F').astype('int')
    sort = np.argsort(zigzagOrdered)      

    for linha in np.arange(0,tam[0],8): 
        for coluna in np.arange(0,tam[1],8):  
            bloco = quant[linha:linha+8,coluna:coluna+8]
            #FAZ A INDEXAÇÃO EM ZIG-ZAG DOS COEFICIENTES AC do bloco presente
            
            #vamos a cada pedaço de 64 em 64 numeros, realizamos flatten em ordem F (por colunas),
            #e ordenamos esse bloco com o "sort" do zig zag
            Bloco = bloco.flatten(order='F')
            copia = Bloco[sort]
  
            #inicializamos variáveis uteis
            posSeg = 0
            zeros = 0
            EOB = True
            
            #copia = copia[1:]                
            
            while(EOB):
                if(sum(abs(copia[posSeg:]))==0):
                    bin_EOB = K5[(0, 0)]
                    final.append(bin_EOB)
                    EOB = False
                    break
                elif(zeros>15):
                    posSeg -= 1
                    cod_huffman = K5[(15,0)]
                    final.append(cod_huffman)
                    zeros = 0    
                elif(copia[posSeg] == 0):
                    zeros += 1
                    posSeg += 1
                else:
                    if(copia[posSeg]<0):
                        #SE FOR NEGATIVO
                        #exemplo para o número "-1": sem o [2:], ficaria '-0b1'. COm [2:] fica 'b1'
                        bin_neg = bin(int(copia[posSeg]))[2:] 
                        #vai buscar o complemento: ex para "-1": binario 1, passa a 0
                        amplitude_bin = Complemento(bin_neg)        
                    else:
                        #SE FOR POSITIVO, apenas basta converter para binário
                        amplitude_bin = bin(int(copia[posSeg]))[2:]
                    
                    grandeza = len(amplitude_bin)    
                    cod_huffman = K5[(zeros,grandeza)]
                    codigo_huffman_AC = cod_huffman + amplitude_bin    
                    final.append(codigo_huffman_AC)
                    zeros = 0
                    posSeg += 1
                    
    final2 = ''.join(final)
                    
    return final2
    
''' Descodificação dos componenetes AC '''
def descodificadorAC(array,K5,altura,largura):
    
    final = np.zeros(8*8)
    
    posSeg = 0
    pos = 0
    array_blocos = np.zeros(shape=(int(altura*8),int(largura*8)))
    linha = 0
    coluna = 0
    
    while posSeg < len(array):
        
        for par_valores, binarios in K5.items():
            if array[posSeg:posSeg + len(binarios)] == binarios:
                run = par_valores[0]
                ampl = par_valores[1]
                
                pos += run
                posSeg += len(binarios)
                
                if(run == 0 and ampl == 0):
                    if(coluna == (largura*8)):
                        coluna = 0
                        linha += 8
                       
                    array_blocos[linha:linha+8,coluna:coluna+8] = final.reshape(8,8)

                    coluna += 8
                    
                    final = np.zeros(8*8)
                    pos = 0
                    
                elif(run!=15 and ampl!=0) or (run!=0 and ampl!=0):
                    bin_conv = array[posSeg:posSeg+ampl]
                    
                    if bin_conv[0] == "0":
                        final[pos] = -(int(Complemento(bin_conv),2))
                    else:
                        final[pos] = int(bin_conv,2)
                    
                    pos += 1
                    posSeg += ampl

                break

    return array_blocos

