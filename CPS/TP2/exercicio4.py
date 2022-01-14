import numpy as np
import scipy.io.wavfile as wav 
from exercicio1 import *
H = np.array([[0, 1, 1],[1, 1, 0],[1, 0, 1],[1, 1, 1],
              [1, 0, 0],[0, 1, 0],[0, 0, 1]])

def retiraBitsAdicionados(lista):
    quantBITS = lista[:2]
    c = np.delete(lista,[0,1])
    return c , quantBITS

def mensagem(lista):
    copia = lista.copy()
    copia.resize(((int)(len(lista)/7),7))
    mensagem = copia
    return mensagem

def Sindroma(lista):
    s =map(lambda x: np.dot(x,H)%2,lista)
    s = np.array(list(s))
    return s

def correccaoDoErro(sindroma,mensagem,quantBits):
    s = sindroma
    a = map(lambda x: np.sum((x == H)*1.0,1),s)
    a = np.array(list(a))
    b = filter(lambda x: np.argwhere(x == 3),a)
    b = np.array(list(b))
    somaDecadaIndiceDeS = map(lambda x: (np.sum(x)),s)
    somaDecadaIndiceDeS = np.array(list(somaDecadaIndiceDeS))
    indiceDifDe0 = np.argwhere(somaDecadaIndiceDeS!=0)
    if(len(indiceDifDe0) != 0):
        indiceDeErro = np.argwhere(b[0] > 2)
        l = indiceDifDe0[0][0]
        c = indiceDeErro[0][0]
        mensagem[l][c] = (mensagem[l][c] + 1)%2
    mL = [mens[:4] for mens in mensagem]
    mL = np.array(mL)
    bits = arrayDeCod(quantBits,len(quantBits))
    nINTdeBits = binTOint(bits,len(quantBits))
    bitsAdeixar = mL[-1][:4-nINTdeBits[0]]
    mLsemUltimaLinha = np.delete(mL , [(len(mL.flatten())-4),(len(mL.flatten())-3),
                        (len(mL.flatten())-2),(len(mL.flatten())-1)])
    mL = np.hstack((mLsemUltimaLinha,bitsAdeixar))
    copia = mL.copy()
    return copia
