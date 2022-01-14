import numpy as np
import signal
from scipy import special
import scipy.io.wavfile as wav
import math
from ex1 import *
from ex2 import *
from ex3 import *
from Trab1exercicio3 import *
from Trab1exercicio5 import *
from Trab2exercicio1 import *
from Trab2exercicio3 import *
from Trab2exercicio4 import *


sampleRate,data = wav.read("sound/bM.wav")
data = np.array(data,'int64')
nBits = np.array([3,5,8])
pot = np.array([0.5, 1, 2, 4])
P = 8
A = 1


q8 = quantizacao(data,nBits[2])
ib8 = intTObin(q8[0],nBits[2])
hamming8 = hamming74(ib8)
retiraBitsAdicionados8 = retiraBitsAdicionados(hamming8)
manch8 = manch(P,A,retiraBitsAdicionados8[0])

canal_AWGN8_0 = canal_AWGN(manch8,pot[0])
canal_AWGN8_1 = canal_AWGN(manch8,pot[1])
canal_AWGN8_2 = canal_AWGN(manch8,pot[2])
canal_AWGN8_4 = canal_AWGN(manch8,pot[3])

filtroadoptado8_0 = filtroadoptado(canal_AWGN8_0,0,P)
filtroadoptado8_1 = filtroadoptado(canal_AWGN8_1,0,P)
filtroadoptado8_2 = filtroadoptado(canal_AWGN8_2,0,P)
filtroadoptado8_3 = filtroadoptado(canal_AWGN8_4,0,P)

BER8_0 = np.sum(((retiraBitsAdicionados8[0] + filtroadoptado8_0)%2)
                )/len(retiraBitsAdicionados8[0])
BER8_1 = np.sum(((retiraBitsAdicionados8[0] + filtroadoptado8_1)%2)
                )/len(retiraBitsAdicionados8[0])
BER8_2 = np.sum(((retiraBitsAdicionados8[0] + filtroadoptado8_2)%2)
                )/len(retiraBitsAdicionados8[0])
BER8_3 = np.sum(((retiraBitsAdicionados8[0] + filtroadoptado8_3)%2)
                )/len(retiraBitsAdicionados8[0])

def berTeorico(x):
    berT = 0.5 * special.erfc(np.sqrt(((A**2)*P)/(2 * x)))
    return berT

BERT8_0 = berTeorico(pot[0])
BERT8_1 = berTeorico(pot[1])
BERT8_2 = berTeorico(pot[2])
BERT8_3 = berTeorico(pot[3])

mensagem8_0 = mensagem(filtroadoptado8_0)
mensagem8_1 = mensagem(filtroadoptado8_1)
mensagem8_2 = mensagem(filtroadoptado8_2)
mensagem8_4 = mensagem(filtroadoptado8_3)

sindroma8_0 = Sindroma(mensagem8_0)
sindroma8_1 = Sindroma(mensagem8_1)
sindroma8_2 = Sindroma(mensagem8_2)
sindroma8_4 = Sindroma(mensagem8_4)

correccaoDoErro8_0 = correccaoDoErro(sindroma8_0,mensagem8_0
                                     ,retiraBitsAdicionados8[1])
correccaoDoErro8_1 = correccaoDoErro(sindroma8_0,mensagem8_1
                                     ,retiraBitsAdicionados8[1])
correccaoDoErro8_2 = correccaoDoErro(sindroma8_0,mensagem8_2
                                     ,retiraBitsAdicionados8[1])
correccaoDoErro8_4 = correccaoDoErro(sindroma8_0,mensagem8_4
                                     ,retiraBitsAdicionados8[1])


BER8_0L = np.sum(((ib8 + correccaoDoErro8_0)%2)
                )/len(ib8)
BER8_1L = np.sum(((ib8 + correccaoDoErro8_1)%2)
                )/len(ib8)
BER8_2L = np.sum(((ib8 + correccaoDoErro8_2)%2)
                )/len(ib8)
BER8_3L = np.sum(((ib8 + correccaoDoErro8_4)%2)
                )/len(ib8)

resize_CDE8_0 = arrayDeCod(correccaoDoErro8_0,nBits[2])
resize_CDE8_1 = arrayDeCod(correccaoDoErro8_1,nBits[2])
resize_CDE8_2 = arrayDeCod(correccaoDoErro8_2,nBits[2])
resize_CDE8_3 = arrayDeCod(correccaoDoErro8_4,nBits[2])

descodificacao8_0 = binTOint(resize_CDE8_0,nBits[2])
descodificacao8_1 = binTOint(resize_CDE8_1,nBits[2])
descodificacao8_2 = binTOint(resize_CDE8_2,nBits[2])
descodificacao8_3 = binTOint(resize_CDE8_3,nBits[2])

desq8_0 = lambda x : q8[2][descodificacao8_0]
desq8_1 = lambda x : q8[2][descodificacao8_1]
desq8_2 = lambda x : q8[2][descodificacao8_2]
desq8_3 = lambda x : q8[2][descodificacao8_3]

desq8_0 = desq8_0(descodificacao8_0)
desq8_1 = desq8_1(descodificacao8_0)
desq8_2 = desq8_2(descodificacao8_0)
desq8_3 = desq8_3(descodificacao8_0)

erroo = erroQ(data,8)
SNR_I = SNRP(erroo,data)
erro8_0 = desq8_0 - data
erro8_1 = desq8_1 - data
erro8_2 = desq8_2 - data
erro8_3 = desq8_3 - data

SNR8_0 = SNRP(erro8_0,data)
SNR8_1 = SNRP(erro8_1,data)
SNR8_2 = SNRP(erro8_2,data)
SNR8_3 = SNRP(erro8_3,data)

if __name__ == "__main__":
    print("SNR")
    print(SNR8_0)
    print(SNR8_1)
    print(SNR8_2)
    print(SNR8_3)

    print("SNR inicial")
    print(SNR_I)

    print("BER")
    print(BER8_0)
    print(BER8_1)
    print(BER8_2)
    print(BER8_3)

    print("BERT")
    print(BERT8_0)
    print(BERT8_1)
    print(BERT8_2)
    print(BERT8_3)

    print("BERL")
    print(BER8_0L)
    print(BER8_1L)
    print(BER8_2L)
    print(BER8_3L)


    plt.plot(desq8_0)
    plt.plot(q8[1])
    plt.show()

    plt.plot(desq8_1)
    plt.plot(q8[1])
    plt.show()
    
    plt.plot(desq8_2)
    plt.plot(q8[1])
    plt.show()

    plt.plot(desq8_3)
    plt.plot(q8[1])
    plt.show()
