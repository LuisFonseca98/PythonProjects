# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:24:48 2020

@author: Rodrigo
"""

def readFile(filename):
    
    with open(filename, 'rb') as ficheiro:
        fileread = [byte for byte in bytearray(ficheiro.read())]
        
        
    array_8bits = []
    for i in range(len(fileread)):
        numero = format(fileread[i], '0%db'%8)
        array_8bits.append(numero)
        
    string_8bits_seguidos = ''.join(array_8bits)
    
    slicer_header = slice(0,3)
    bits_adicionados = int(string_8bits_seguidos[slicer_header], 2)
    slicer_newString_in = slice(3, len(string_8bits_seguidos)-bits_adicionados)
    string_withoutBitStuffing = string_8bits_seguidos[slicer_newString_in]
    array_withoutBitStuffing = list(string_withoutBitStuffing)

    ac_length = int(''.join(array_withoutBitStuffing[:20]),2)
    del(array_withoutBitStuffing[:20])
    
    AC = ''.join(array_withoutBitStuffing[:ac_length])
    del(array_withoutBitStuffing[:ac_length])
    
    dc_length = int(''.join(array_withoutBitStuffing[:20]),2)
    del(array_withoutBitStuffing[:20])
    
    DC = ''.join(array_withoutBitStuffing[:dc_length])


    return AC, DC
    
if __name__ == '__main__':
    
    readFile("lena_25.txt")