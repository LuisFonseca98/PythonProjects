from Trab1exercicio2 import criacaoIntervalosQuantizacao
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt 


tipo = "midrise"
def quantizacao(data,nBits):
    vMax=np.max(data)
    intervalosQuantizacao,intervalosDecisao = criacaoIntervalosQuantizacao(vMax,nBits,tipo)
    indicesDecisaoResultantes = np.searchsorted(intervalosDecisao,data)
    xq = indicesDecisaoResultantes
    vq = lambda b : intervalosQuantizacao[xq]
    return (xq,vq(data),intervalosQuantizacao)

