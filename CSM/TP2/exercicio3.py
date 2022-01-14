# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:41:22 2020

@author: Rodrigo
"""

from exercicio5 import readFile2Array
from exercicio1 import gen_huff_table
import numpy as np

def decode_huff(string_in, code_table):
    
    slicer_header = slice(0,3)
    bits_adicionados = int(string_in[slicer_header], 2)
    slicer_newString_in = slice(3, len(string_in)-bits_adicionados)
    string_withoutBitStuffing = string_in[slicer_newString_in]
    array_withoutBitStuffing = list(string_withoutBitStuffing)
    
    numeroSimbolos = int(string_withoutBitStuffing[slice(0, 8)], 2)
    del(array_withoutBitStuffing[:8])
    
    simbolos = []
    huffmanCode = []
    
    for i in range(numeroSimbolos):
        simbolo = int(''.join(array_withoutBitStuffing[:8]),2)
        simbolos.append(str(simbolo))
        del(array_withoutBitStuffing[:8])
        dimensaoHuffman = int(''.join(array_withoutBitStuffing[:5]), 2)
        del(array_withoutBitStuffing[:5])
        huffman = ''.join(array_withoutBitStuffing[:dimensaoHuffman])
        huffmanCode.append(huffman)
        del(array_withoutBitStuffing[:dimensaoHuffman])
        
    tabela = zip(simbolos, huffmanCode)

    # Trocar as keys por os values
    tabela_dict = dict((i[1], i[0]) for i in tabela)
    
    mensagem = ''.join(array_withoutBitStuffing)

    index = 0
    array_out = []

    while index < len(mensagem):
        for key in tabela_dict:
            if mensagem[index : index + len(key)] == key:
                array_out.append(tabela_dict[key])
                index += len(key)
                break
            
    return np.array(array_out).astype(int)


if __name__ == '__main__':
    
    filename = "teste.txt"
    string_lida = readFile2Array(filename)
    simbolo = [0, 1, 2, 3, 4]
    ocurrencias = np.array([2, 3, 1, 2, 1])
    tabela, frequencias = gen_huff_table(simbolo, ocurrencias)
    array_out = decode_huff(string_lida, tabela)
    print("Mensagem descodificada:",array_out)