# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:47:17 2020

@author: Rodrigo
"""

import numpy as np
from exercicio1 import gen_huff_table
import re

def writeArray2File(mensagem, file_name, symbol_code_table):
    
    stringmensagem = []
    if(isinstance(mensagem[0], str) ):
        stringmensagem = ''.join(mensagem)
        #array = list(map(int,array_sem_plicas))
    elif(isinstance(mensagem[0], int)):
        stringmensagem = "".join([str(a) for a in mensagem])
        

    stringTabela = ""
    primeiros8bits = format(len(symbol_code_table), '0%db'%8)
    stringTabela += primeiros8bits
    for i in range(len(symbol_code_table)):
        segundos8bits = format(int(symbol_code_table[i][0]), '0%db'%8)
        bits5indicativos = format(len(symbol_code_table[i][1]), '0%db'%5)
        huffman8bits = symbol_code_table[i][1]
        stringTabela += segundos8bits + bits5indicativos + huffman8bits
        

    tamanhoRestante = 0
    if((len(stringTabela) + len(stringmensagem) + 3) % 8 != 0):
        tamanhoRestante = 8 - ((len(stringTabela) + len(stringmensagem) + 3) % 8)
        
    header = format(tamanhoRestante, '0%db'%3) 
    zerosAdicionais = tamanhoRestante * '0'
    
    stringFinal = header+stringTabela+stringmensagem+zerosAdicionais
    
    
    #FORMA 1
    
    binaryArray = re.findall('[01]{8}', stringFinal)
    intArray = [int(i, 2) for i in binaryArray]
    finalArray = np.array(intArray, dtype = 'uint8')
    byteArray = bytearray(finalArray)
    
    #FORMA 2
#    arrayFinal = np.array(list(map(int,stringFinal)))
#    array_reshaped = arrayFinal.reshape(-1,8)
#    array_inteiros = np.packbits(array_reshaped)
#    byteArray = bytearray(array_inteiros)    
#    
    newFile = open(file_name, "wb")
    # write to file
    newFile.write(byteArray)
    newFile.close()
#    
if __name__ == '__main__':
    simbolo = [0, 1, 2, 3, 4]
    ocorrencias = np.array([2, 3, 1, 2, 1])
    tabela, frequencias = gen_huff_table(simbolo, ocorrencias)
    array = ['00', '00', '101', '01', '101', '100']
    filename = "teste.txt"
    writeArray2File(array, filename, tabela)
    print("Ficheiro escrito com sucesso!")