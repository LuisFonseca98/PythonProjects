import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg
from exercicio1 import *
from exercicio2 import *
from exercicio3 import *
from exercicio4 import *

#c - mensagem inicial com o hamming
#erro - mensagem passada com o erro

#c´ - sinal dps da codificacao(inteiro para binario), descodificacao(binario para inteiro)
#mensagemCorrigida - sinal dps da correcao de erro
arrayNBits = [3,5,8]#numero de bits a usar

c = np.array([0,0,1,0,1,0])#mensagem
hamming = hamming74(c)#passar pela mensagem hamming74(para a detecao do erro), caso a quantidade de bits nao for divisel por 4, ele adiciona 0
mensagemMatrix,quantidadeBits = retiraBitsAdicionados(hamming) #elimina os bits
x = mensagemMatrix


#Ber com 0.2
erro = 1*np.logical_xor(x,np.random.binomial(1,0.2,len(x))) #cria o erro
y = (x + erro)%2
BER = np.sum(((x + y)%2)/len(x)) #calcula o BER(em %)
#BER´
menAposCanal = mensagem(y)#chamar o metodo da mensagem, pois ele so vai usar 2bits
sindroma = Sindroma(menAposCanal) #chamar o sindroma para corrigir o erro
mensagemCorrigida = correccaoDoErro(sindroma,menAposCanal,quantidadeBits) #corrige o erro
BERlinha = np.sum(((c + mensagemCorrigida)%2)/len(c))


#BER com 0.3
erro2 = 1*np.logical_xor(x,np.random.binomial(1,0.3,len(x))) #cria o erro
y2 = (x + erro2)%2
BER2 = np.sum(((x + y2)%2)/len(x)) #calcula o BER(em %)
#BER´
menAposCanal2 = mensagem(y2)#chamar o metodo da mensagem, pois ele so vai usar 2bits
sindroma2 = Sindroma(menAposCanal2) #chamar o sindroma para corrigir o erro
mensagemCorrigida2 = correccaoDoErro(sindroma2,menAposCanal2,quantidadeBits) #corrige o erro
BERlinha2 = np.sum(((c + mensagemCorrigida2)%2)/len(c))


#Ber com 0.5
erro3 = 1*np.logical_xor(x,np.random.binomial(1,0.5,len(x))) #cria o erro
y3 = (x + erro3)%2
BER3 = np.sum(((x + y3)%2)/len(x)) #calcula o BER(em %)
#BER´
menAposCanal3 = mensagem(y3)#chamar o metodo da mensagem, pois ele so vai usar 2bits
sindroma3 = Sindroma(menAposCanal3) #chamar o sindroma para corrigir o erro
mensagemCorrigida3 = correccaoDoErro(sindroma3,menAposCanal3,quantidadeBits) #corrige o erro
BERlinha3 = np.sum(((c + mensagemCorrigida3)%2)/len(c))


###########################################SNR###################################
sampleRate,data = wav.read("sound/CPS_Exercicio1.wav") #sinal
data = np.array(data[:,0],'int32')#:0, porque o som é stereo e é preciso retirar cada 2 amostra

#Amostragem
FsAmost = 8000

#quantizacao
#Para 3 bits
sinalB3,vq3 = quantizacao(data,arrayNBits[0])
intParaBin3 = intTObin(sinalB3,arrayNBits[0])
sinalCodificadoB3 = arrayDeCod(intParaBin3,arrayNBits[0])#sinal codificado
sinalDescodificadoB3 = binTOint(sinalCodificadoB3,arrayNBits[0]) #sinal Descodificado

SNR_CodificadoB3 = SNR(sinalCodificadoB3,arrayNBits)
SNR_DescodificadoB3 = SNR(sinalDescodificadoB3,arrayNBits)

#Para 5 bits
sinalB5,vq5 = quantizacao(data,arrayNBits[1])
intParaBin5 = intTObin(sinalB5,arrayNBits[1])
sinalCodificadoB5 = arrayDeCod(intParaBin5,arrayNBits[1])#sinal codificado
sinalDescodificadoB5 = binTOint(sinalCodificadoB5,arrayNBits[1]) #sinal Descodificado

SNR_CodificadoB5 = SNR(sinalB5,arrayNBits)
SNR_DescodificadoB5 = SNR(sinalDescodificadoB5,arrayNBits)

#Para 8 bits
sinalB8,vq8 = quantizacao(data,arrayNBits[2])
intParaBin8 = intTObin(sinalB8,arrayNBits[2])
sinalCodificadoB8 = arrayDeCod(intParaBin8,arrayNBits[2])#sinal codificado
sinalDescodificadoB8 = binTOint(sinalCodificadoB8,arrayNBits[2]) #sinal Descodificado

SNR_CodificadoB8 = SNR(sinalB8,arrayNBits)
SNR_DescodificadoB8 = SNR(sinalDescodificadoB8,arrayNBits)

if __name__ == "__main__":
    print("valor do BER1: ")
    print(BER)
    print("valor do BERlinha1:")
    print(BERlinha)
    print("----------")
    print("valor do BER2:")
    print(BER2)
    print("valor do BERlinha2:")
    print(BERlinha2)
    print("---------------------")
    print("valor do BER3:")
    print(BER3)
    print("valor do BERlinha3:")
    print(BERlinha3)
    plt.title("BER e BERLinha")
    valoresBER = np.hstack((BER,BER2,BER3))
    valoresBERlinha = np.vstack((BERlinha,BERlinha2,BERlinha3))
    plt.stem(valoresBERlinha,valoresBER)
    plt.show()

    
    print()
    print("SNR a 3bits")
    print(SNR_CodificadoB3)
    print(SNR_DescodificadoB3)
    print()
    print("SNR a 5bits")
    print(SNR_CodificadoB5)
    print(SNR_DescodificadoB5)
    print()
    print("SNR a 8bits")
    print(SNR_CodificadoB8)
    print(SNR_DescodificadoB8)
    
    wav.write("sound/Sinal quantizado a 3bits.wav",FsAmost,vq3.astype('int16'))
    wav.write("sound/Sinal quantizado a 5bits.wav",FsAmost,vq5.astype('int16'))
    wav.write("sound/Sinal quantizado a 8bits.wav",FsAmost,vq8.astype('int16'))
    wav.write("sound/Sinal descodificado a 3bits.wav",FsAmost,vq3.astype('int16'))
    wav.write("sound/Sinal descodificado a 5bits.wav",FsAmost,vq5.astype('int16'))
    wav.write("sound/Sinal descodificado a 8bits.wav",FsAmost,vq8.astype('int16'))

