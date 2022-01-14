import numpy as np
import matplotlib as plt
import scipy.io.wavfile as wav


def criacaoIntervalosQuantizacao(Vmax,nBits,tipo):
    delta = (2*Vmax)/2**nBits
    if(tipo == "midrise"):
        gamaQuantificador = np.arange((-Vmax+delta/2),(Vmax-delta/2)+delta,delta)
        decisao = np.arange(-Vmax + delta,Vmax ,delta)
    else:
        gamaQuantificador = np.arange((-Vmax + delta),(Vmax) + delta ,delta)
        decisao = np.arange(-Vmax+delta/2,Vmax,delta)

    return [gamaQuantificador,decisao]

