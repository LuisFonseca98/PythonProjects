# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:01:42 2020

@author: Rodrigo
"""

from heapq import heappush, heappop
import numpy as np

def gen_huff_table(symbol_list,symbol_prob):
    #converte o array do numero de ocorrencias num array de inteiros
    nOcorrencias = symbol_prob.astype(int)
    #garantir que o array de simbolos é lido em formato string
    symbol_list_string = np.array(symbol_list).astype(str)

    # realiza um zip, ou seja, efetua uma transformacao de um array para passar a mostrar
    # [simb, nOcorrencias]
    array_zipado = zip(symbol_list_string,nOcorrencias)
    
    #ordena o array zip pelo valor do numero de ocorrencias
    array_ordenado = sorted(array_zipado, key=lambda tup: tup[1])

    # permite obter um array da forma [ocorrencias, [simbolo, codigoHuffman]]
    array = [[ocorrencias,[simbolo, ""]] for simbolo, ocorrencias in array_ordenado] 

    array_sem_zeros = []
    
    # retira os simbolos que teem numero de ocorrencias nulos
    for i in range(len(array)):
        if array[i][0] != 0:
            array_sem_zeros.append(array[i])
            
    # coloca as frequencias dos simbolos que nao conteem ocorrencias nulas num array 
    frequencias = []
    for i in range(len(array_sem_zeros)):
        frequencias.append(array_sem_zeros[i])
        
    
    # realizar o código de Huffman, atribuindo valores binarios (0 ou 1) consoante
    # o ramo percorrido
    array_final = []
    #vamos realizar este processo até ter apenas um valor no array
    while len(array_sem_zeros) > 1:
        #retiramos o valor de menor ocorrencia do array_sem_zeros
        menor_ocorrencia = heappop(array_sem_zeros)
        #retiramos o segundo valor de menor ocorrencia do array_sem_zeros (que passou a ser
        #a de menor ocorrência, pois heappop retira o valor encontrado do array)
        segunda_menor_ocorrencia = heappop(array_sem_zeros)
        
        #atribuicao de 0 ou 1, consoante o ramo percorrido
        for i in menor_ocorrencia[1:]:
            i[1] = '1' + i[1]            
        for i in segunda_menor_ocorrencia[1:]:
            i[1] = '0' + i[1]
            
        #coloca o valor obtida da soma das menores ocorrências dentro do array novamente
        heappush(array_sem_zeros, [menor_ocorrencia[0] + segunda_menor_ocorrencia[0]] + \
                                   menor_ocorrencia[1:] + segunda_menor_ocorrencia[1:])
        
    #ordena o array sem zeros, e atribui o valor a variavel array_final
    array_final = (array_sem_zeros[0])[slice(1, len(array_sem_zeros[0]))]
    array_final.sort(key=lambda x: int(x[0]))

    #array_final = sorted(heappop(array_sem_zeros)[1:])
    

    return array_final, frequencias


if __name__ == '__main__':
    
    #simb = ["a", "b", "c", "d", "e"]
    ##simb = ["0", "1", "2", "3", "4"]
    #ocurr = np.array([20, 10, 35, 2, 5])
    simbolo = np.array([1, 2, 3, 4, 10])
    ocurrencias = np.array([2, 3, 1, 2, 1])
    tabela, freq = gen_huff_table(simbolo, ocurrencias)
    print(tabela)



