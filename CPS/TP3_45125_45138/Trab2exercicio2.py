import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from Trab2exercicio1 import *
from Trab1exercicio3 import *
from Trab1exercicio5 import *
from scipy import signal as sg


nBits = [3,5,8]

sampleRate,data = wav.read("sound/CPS_Exercicio1.wav");
data = np.array(data[:,0],'int16')
##3bits
sinalq3 , vq3, criarTab3 = quantizacao (data,nBits[0])
intParaBin3 = intTObin(sinalq3,nBits[0])
arrayDeCodificacao3 = arrayDeCod(intParaBin3,nBits[0])
arrayDescodificacao3 = binTOint(arrayDeCodificacao3,nBits[0])
desq3 = lambda x : criarTab3[arrayDescodificacao3]
desq3 = desq3(arrayDescodificacao3)
##5bits
sinalq5 , vq5, criarTab5 = quantizacao (data,nBits[1])
intParaBin5 = intTObin(sinalq5,nBits[1])
arrayDeCodificacao5 = arrayDeCod(intParaBin5,nBits[1])
arrayDescodificacao5 = binTOint(arrayDeCodificacao5,nBits[1])
desq5 = lambda x : criarTab5[arrayDescodificacao5]
desq5 = desq5(arrayDescodificacao5)
##8bits
sinalq8 , vq8, criarTab8 = quantizacao (data,nBits[2])
intParaBin8 = intTObin(sinalq8,nBits[2])
arrayDeCodificacao8 = arrayDeCod(intParaBin8,nBits[2])
arrayDescodificacao8 = binTOint(arrayDeCodificacao8,nBits[2])
desq8 = lambda x : criarTab8[arrayDescodificacao8]
desq8 = desq8(arrayDescodificacao8)

if __name__ == "__main__":
    snrAudioInicial3 = SNR(sinalq3,nBits)
    snrAudioInicial5 = SNR(sinalq5,nBits)
    snrAudioInicial8 = SNR(sinalq8,nBits)
    erroq3 = erroQ(sinalq3,nBits[0])
    erroq5 = erroQ(sinalq5,nBits[1])
    erroq8 = erroQ(sinalq8,nBits[2])
    snrp3 = SNRP(erroq3,sinalq3)
    snrp5 = SNRP(erroq5,sinalq5)
    snrp8 = SNRP(erroq8,sinalq8)
    snrAudio3 = SNR(arrayDescodificacao3,nBits)
    snrAudio5 = SNR(arrayDescodificacao5,nBits)
    snrAudio8 = SNR(arrayDescodificacao8,nBits)
    print("Snr Pratico")
    print("Para 3 bits")
    print(snrAudioInicial3[0])
    print("Para 5 bits")
    print(snrAudioInicial5[1])
    print("Para 8 bits")
    print(snrAudioInicial8[2])
    print("Snr Teórico")
    print("Para 3 bits")
    print(snrp3)
    print("Para 5 bits")
    print(snrp5)
    print("Para 8 bits")
    print(snrp8)
    wav.write("sound/exercicio2_som_descodificado_a_3bits.wav",sampleRate,desq3.astype('int16'))
    wav.write("sound/exercicio2_som_descodificado_a_5bits.wav",sampleRate,desq5.astype('int16'))
    wav.write("sound/exercicio2_som_descodificado_a_8bits.wav",sampleRate,desq8.astype('int16'))


