import numpy as np
p = np.arange(0,100,1)
nBits = 4

def intTObin(lista,nBits):
    intToBin = map(lambda x: (np.binary_repr(x,nBits)),lista) 
    intToBin1 = list(intToBin)
    intToBin2 = ''.join(intToBin1)
    intToBin3 = ' '.join(intToBin2)
    intToBin4 = intToBin3.split(" ")
    return np.array(list(intToBin4)).astype(int)

def arrayDeCod(lista,nBits):
    copia = lista.copy()
    copia.resize(((int)(len(lista)/nBits), nBits))
    return copia

def binTOint(lista,nBits):
    c = lista.astype(str)
    binto = map(lambda x : ''.join(c[x]),range(len(c)))
    binto1 = list(binto) 
    binTOint = map(lambda x: int(binto1[x],2),range(len(binto1))) 
    return np.array(list(binTOint)).astype(int) 

