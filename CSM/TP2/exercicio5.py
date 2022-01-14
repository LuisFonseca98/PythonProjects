# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:58:17 2020

@author: Rodrigo
"""
            
def readFile2Array(file_name):

    with open(file_name, 'rb') as ficheiro:
        fileread = [byte & 255 for byte in bytearray(ficheiro.read())]
        
        
    array_8bits = []
    for i in range(len(fileread)):
        numero = format(fileread[i], '0%db'%8)
        array_8bits.append(numero)
        
    string_8bits_seguidos = ''.join(array_8bits)
        
#    array_chars = data[1:]
#    novo_array = map(ord,array_chars)
#    array_binario = bin_converter(novo_array)
#    array_binario = ''.join(array_binario)
    return string_8bits_seguidos

if __name__ == '__main__':
    
    filename = "teste.txt"
    string_lida = readFile2Array(filename)
    print(string_lida)