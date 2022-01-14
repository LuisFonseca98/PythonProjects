from Trab1exercicio2 import criacaoIntervalosQuantizacao
import scipy.io.wavfile as wav
import numpy as np

nBits = 3
tipo = "midrise"
def quantizacao(data,nBits):
    vMax=np.max(data)
    intervalosQuantizacao,intervalosDecisao = criacaoIntervalosQuantizacao(vMax,nBits,tipo)
    indicesDecisaoResultantes = lambda indices : np.searchsorted(intervalosDecisao,data)
    xq = indicesDecisaoResultantes(data)
    vq = lambda b : intervalosQuantizacao[xq]
    return (xq,vq(data))



