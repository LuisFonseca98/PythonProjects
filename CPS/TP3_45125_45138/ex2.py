import numpy as np
from ex1 import *

def filtroadoptado(sinal,limiarDedecisao,P):
    MtempoBit = int(P/2)
    sinal = sinal.flatten()
    copiaSinal = sinal.copy()
    copiaSinal.resize(((int)(len(sinal)/P),P))
    c = np.hstack((np.ones(MtempoBit)*-1,np.ones(MtempoBit)))
    resultado = map(lambda x: np.sum(x * c),copiaSinal)
    resultado = np.array(list(resultado))
    func = map(lambda x: 1 if(x >limiarDedecisao) else 0,resultado)
    return np.array(list(func))


def arrayDeCod(lista,nBits):
    copia = lista.copy()
    copia.resize(((int)(len(lista)/nBits), nBits))
    return copia



