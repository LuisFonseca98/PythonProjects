# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:14:10 2020

@author: Rodrigo
"""

from exercicio1 import gen_huff_table
import numpy as np

def encode_huff(message,symbol_code_table):
    
    #Garantir que os simbolos sao lidos em formato string
    msgString = []
    if(isinstance(message[0], str)):
        msgString = message
    else:
        msgString = [str(i) for i in message]
        
        
    array_out = []
    simbolo = list(msgString)
    tabela = dict(symbol_code_table)
    for i in simbolo:
        if i in tabela:
            array_out.append(tabela[i]) 
        else:
            print("A Letra/Número " + str(i) + " não se encontra na lista de símbolos disponível")
    return array_out


if __name__ == '__main__':
    
    simbolo = [0, 1, 2, 3, 4]
    ocurrencias = np.array([2, 3, 1, 2, 1])
    tabela, frequencias = gen_huff_table(simbolo, ocurrencias)
    mensagem = [1, 1, 2, 3, 2, 4]
    print("Codificação da mensagem '", mensagem,"'")
    codificacao = encode_huff(mensagem, tabela)
    print(codificacao)