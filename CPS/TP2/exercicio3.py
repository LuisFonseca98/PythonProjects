import numpy as np
from exercicio1 import *
G = np.array([[1,0,0,0,0,1,1],[0,1,0,0,1,1,0],[0,0,1,0,1,0,1],[0,0,0,1,1,1,1]])

def hamming74(lista):
    quantBITS = np.array([0, 0])
    if (lista.size%4 != 0):
        x = (4 - lista.size%4)
        BITSredond = intTObin([0],x)
        lista = np.hstack((lista,BITSredond))
        quantBITS = intTObin([x],2) 
    copia = lista.copy()
    copia.resize(((int)(len(lista)/4),4))
    hamm = map(lambda x : np.dot(x,G)%2,copia)
    hamm = np.array(list(hamm))
    hamm = hamm.flatten() #retorna um nova array, com uma so dimensao
    hamm = np.hstack((quantBITS,hamm))
    return hamm
