import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from exercicio1 import *
from Trab1exercicio3 import *
from Trab1exercicio5 import *
from scipy import signal as sg


nBits = [3,5,8]
nPontos = 4096
sampleRate,data = wav.read("sound/CPS_Exercicio1.wav");
data = np.array(data[:,0],'int16')
FsAmostragem = 8000

sinalq3 , vq3 = quantizacao (data,nBits[0])
intParaBin3 = intTObin(sinalq3,nBits[0])
arrayDeCodificacao3 = arrayDeCod(intParaBin3,nBits[0])
arrayDescodificacao3 = binTOint(arrayDeCodificacao3,nBits[0])

sinalq5 , vq5 = quantizacao (data,nBits[1])
intParaBin5 = intTObin(sinalq5,nBits[1])
arrayDeCodificacao5 = arrayDeCod(intParaBin5,nBits[1])
arrayDescodificacao5 = binTOint(arrayDeCodificacao5,nBits[1])

sinalq8 , vq8 = quantizacao (data,nBits[2])
intParaBin8 = intTObin(sinalq8,nBits[2])
arrayDeCodificacao8 = arrayDeCod(intParaBin8,nBits[2])
arrayDescodificacao8 = binTOint(arrayDeCodificacao8,nBits[2])


if __name__ == "__main__":
    snrAudioInicial3 = SNR(sinalq3,nBits)
    snrAudioInicial5 = SNR(sinalq5,nBits)
    snrAudioInicial8 = SNR(sinalq8,nBits)
    snrAudio3 = SNR(arrayDescodificacao3,nBits)
    snrAudio5 = SNR(arrayDescodificacao5,nBits)
    snrAudio8 = SNR(arrayDescodificacao8,nBits)
    print("Snr do sinal inicial")
    print("Para 3 bits")
    print(snrAudioInicial3[0])
    print("Para 5 bits")
    print(snrAudioInicial5[1])
    print("Para 8 bits")
    print(snrAudioInicial8[2])
    print("--------------------------")
    print("Snr do sinal descodificado")
    print("Para 3 bits")
    print(snrAudio3[0])
    print("Para 5 bits")
    print(snrAudio5[1])
    print("Para 8 bits")
    print(snrAudio8[2])
    wav.write("sound/exercicio2_som_descodificado_a_3bits.wav",FsAmostragem,vq3.astype('int16'))
    wav.write("sound/exercicio2_som_descodificado_a_5bits.wav",FsAmostragem,vq5.astype('int16'))
    wav.write("sound/exercicio2_som_descodificado_a_8bits.wav",FsAmostragem,vq8.astype('int16'))


