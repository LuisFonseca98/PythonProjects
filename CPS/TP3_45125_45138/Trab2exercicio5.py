import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg
from Trab2exercicio1 import *
from Trab2exercicio2 import *
from Trab2exercicio3 import *
from Trab2exercicio4 import *
from Trab1exercicio5 import *

nBits = [3,5,8]

sampleRate,data = wav.read("sound/CPS_Exercicio1.wav")
data = np.array(data[:,0],'int64')

q8 = quantizacao(data,nBits[2])
ib8 = intTObin(q8[0],nBits[2])
hamm8 = hamming74(ib8)
retira8 = retiraBitsAdicionados(hamm8)

###Para BER de 0.00001
erro8_1 = 1*np.logical_xor(retira8[0]
                        ,np.random.binomial(1,0.00001,len(retira8[0])))
BER_1 = np.sum(((retira8[0] + erro8_1)%2))/len(retira8[0])
mens8_1 = mensagem(erro8_1)
s8_1 = Sindroma(mens8_1)
semE8_1 = correccaoDoErro(s8_1,mens8_1,retira8[1])
BERL_1 = np.sum(((ib8 + semE8_1)%2))/len(ib8)
ac8_1 = arrayDeCod(semE8_1,nBits[2])
bi8_1 = binTOint(ac8_1,nBits[2])
desq8_1 = lambda x : q8[2][bi8_1]
desq8_1 = desq8_1(bi8_1)

###Para para BER de 0.0005
erro8_2 = 1*np.logical_xor(retira8[0]
                        ,np.random.binomial(1,0.0005,len(retira8[0])))
BER_2 = np.sum(((retira8[0] + erro8_2)%2))/len(retira8[0])
mens8_2 = mensagem(erro8_2)
s8_2 = Sindroma(mens8_2)
semE8_2 = correccaoDoErro(s8_2,mens8_2,retira8[1])
BERL_2 = np.sum(((ib8 + semE8_2)%2))/len(ib8)
ac8_2 = arrayDeCod(semE8_2,nBits[2])
bi8_2 = binTOint(ac8_2,nBits[2])
desq8_2 = lambda x : q8[2][bi8_2]
desq8_2 = desq8_2(bi8_2)

#Para BER de 0.1
erro8_3 = 1*np.logical_xor(retira8[0]
                        ,np.random.binomial(1,0.1,len(retira8[0])))
BER_3 = np.sum(((retira8[0] + erro8_3)%2))/len(retira8[0])
mens8_3 = mensagem(erro8_3)
s8_3 = Sindroma(mens8_3)
semE8_3 = correccaoDoErro(s8_3,mens8_3,retira8[1])
BERL_3 = np.sum(((ib8 + semE8_3)%2))/len(ib8)
ac8_3 = arrayDeCod(semE8_3,nBits[2])
bi8_3 = binTOint(ac8_3,nBits[2])
desq8_3 = lambda x : q8[2][bi8_3]
desq8_3 = desq8_3(bi8_3)



if __name__ == "__main__":
    erroo = erroQ(data,8)
    SNR_I = SNRP(erroo,data)
    print("SNR inicial")
    print(SNR_I)
    print("SNR final")
    erro8_3 = desq8_3 - data
    SNR8_3 = SNRP(erro8_3,data)

    print(SNR8_3)
    print("Resultados para Ber Teorico de 0.00001")
    print("BER")
    print(BER_1)
    print("BER linha")
    print(BERL_1)
    print("Resultados para Ber Teorico de 0.0005")
    print("BER")
    print(BER_2)
    print("BER linha")
    print(BERL_2)
    print("Resultados para Ber Teorico de 0.1")
    print("BER")
    print(BER_3)
    print("BER linha")
    print(BERL_3)
    wav.write("sound/Sinal com BER 0.00001.wav",sampleRate,desq8_1.astype('int16'))
    wav.write("sound/Sinal com BER 0.0005.wav",sampleRate,desq8_2.astype('int16'))
    wav.write("sound/Sinal com BER 0.1.wav",sampleRate,desq8_3.astype('int16'))

