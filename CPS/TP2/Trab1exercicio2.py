import numpy as np
import matplotlib as plt

def criacaoIntervalosQuantizacao(Vmax,nBits,tipo):
    delta = (2*Vmax)/2**nBits
    if(tipo == "midrise"):
        gamaQuantificador = np.arange((-Vmax+delta/2),(Vmax-delta/2)+0.00001,delta)
        decisao = np.arange(-Vmax/2 - delta,Vmax/2 + delta +0.00001,delta)
    else:
        gamaQuantificador = np.arange(-Vmax,Vmax,delta)
        decisao = np.arange(-Vmax+delta/2,Vmax/2+delta +0.0001,delta)

    return [gamaQuantificador,decisao]

