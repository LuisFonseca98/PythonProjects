# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:18:52 2020

@author: Rodrigo
"""

from time import time
import os
import cv2
import matplotlib.pyplot as plt
from exercicio1 import gen_huff_table
from exercicio2 import encode_huff
from exercicio3 import decode_huff
from exercicio4 import writeArray2File
from exercicio5 import readFile2Array
import numpy as np
from scipy import stats


# Lê a imagem em níveis de cinzento
x = cv2.imread( "lenac.tif", cv2.IMREAD_GRAYSCALE )
shape = x.shape

# Converte a imagem (matriz) numa sequência de números (array)
xi = x.ravel()

# Calcula o histogram
symbol_ocorr, symbols_list, patches = plt.hist(xi,256,[0,256])
symbol_list = np.arange(0, 256)

# código alínea a) - Gera o código de Huffman
t0 = time()
symbol_code_table, frequencias = gen_huff_table(symbol_list, symbol_ocorr)
t1 = time()
print("----------- Alínea a) ------------")
print("Codificação Huffman:")
print(symbol_code_table)
print()
print("time a) tabela Huffman: ", t1-t0)
print()

def probabilidadeSimbolo(frequencias):
    
    somaOcorrencias = sum([i[0] for i in frequencias])
    
    probabilidades = []
    for i in range(len(frequencias)):
        
        probabilidades.append(frequencias[i][0]/somaOcorrencias)
        
    return probabilidades

def entropia(frequencias):
    """metodo que calcula a entropia usando a biblioteca scipy com o metodo entropy"""

    entropy = stats.entropy(probabilidadeSimbolo(frequencias),None,2.)
    return entropy


def nBits_simbolo(frequencias, tabela):
    
    probabilidades = probabilidadeSimbolo(frequencias)

    L = 0
    for i in range(len(tabela)):
        L += probabilidades[i]*len(frequencias[i][1][1])
    
    return L
    

def eficiencia(entropia, nMedioBits):
    return float(entropia) / float(nMedioBits)


# código alíneas b)

Entropy = entropia(frequencias)
print("Entropia: ", Entropy)
L = nBits_simbolo(frequencias, symbol_code_table)
print("Número médio de bits por símbolo: ", L)
Eficiency = eficiencia(Entropy, L)
print("Eficiência: ", Eficiency)
print()


# código alíneas c) e d) - Codifica e grava ficheiro
binary_codes = encode_huff(xi, symbol_code_table)
t2 = time()
print("A mensagem foi codificada com sucesso, ficando com tamanho: ", len(binary_codes))
print("time c) codificação:", t2-t1)

filename = "LenaCodificada.txt"
writeArray2File(binary_codes, filename, symbol_code_table)
print()
print("Escreveu no ficheiro com sucesso")
print("Ficheiro de tamanho:", os.path.getsize(filename), "bytes")


# código alíneas e) e f) Lê ficheiro e descodifica
binaryArray = readFile2Array(filename)
print()
print("Ficheiro lido com sucesso")

yi = decode_huff(binaryArray, symbol_code_table)
t3 = time()
print("time descodificacao:", t3-t2)

img = np.array(yi).reshape(shape)
cv2.imwrite("lenaDepoisDescodificacao.tif",img)

# código alíneas g)
erro = np.sum(xi - yi)
print("Erro:",erro)
size_ini = os.path.getsize("lenaGray.tif")
size_end = os.path.getsize(filename)
print("taxa: ", 1.* size_ini / size_end)
#plt.show()
#cv2.waitKey(0)
#plt.close("all")
#cv2.destroyAllWindows()