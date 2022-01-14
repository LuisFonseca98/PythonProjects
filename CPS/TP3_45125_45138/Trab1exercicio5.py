import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Trab1exercicio3 import quantizacao
from Trab1exercicio4 import *
sampleRate,data = wav.read("sound/CPS_Exercicio1.wav")
data = np.array(data[:,0],'int16')

R = {3 ,4 ,5 ,6 ,7 ,8}
t = np.linspace(0,1,500)
rampa = signal.sawtooth(2 * np.pi * 5 * t)
#----------------------A------------------------
def sinal(data):
    sinal1 = quantizacao(data,3)[1]
    sinal2 = quantizacao(leiA(87.65,data))[1]
    return sinal1,sinal2

#----------------------B------------------------
def erroQ(data,nBits):
    xn = data
    xq = quantizacao(data,nBits)[1]
    eq=xn-xq
    return eq

#----------------------C------------------------
def SNR(data,R):
    vMax = np.max(data)
    pot = np.sum(np.power(data,2))/len(data)
    snrT = map(lambda x :6.02 * x + 10 * (np.log10((3 * pot) / (vMax**2))),R)
    snrT = np.array(list(snrT))
    return snrT

def SNRP(erroQ,data):
    snrP = 10 * np.log10(np.sum(np.power(data,2))/np.sum(np.power(erroQ,2)))
    return snrP

