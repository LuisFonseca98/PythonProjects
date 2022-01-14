from Trab1exercicio2 import *
from Trab1exercicio3 import *
from Trab1exercicio4 import *
from Trab1exercicio5 import *
from Trab2exercicio1 import *
from Trab2exercicio3 import *
from Trab2exercicio4 import *

from ex2 import *
from ex3 import *
from ex1_GrupoB import *
from ex2_GrupoB import *
from scipy import special
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg

sampleRate,data = wav.read("sound/bM.wav")
data = np.array(data,'int16')
P = 8
A1 = 3
A0 = 1
nBits = 8
sinal,vq,TabelasQuantizacao = quantizacao(data,nBits)
ib8 = intTObin(sinal,nBits)
pot = 0.2

##com modulo de correção de erros
hamming = hamming74(ib8)
retirabits = retiraBitsAdicionados(hamming)
ASK = sinalASK(retirabits[0],P,A1,A0)
canalAWGN = canal_AWGN(ASK,pot)
filtro = filtroASK(canalAWGN,A1,A0,P)
mens = mensagem(filtro)
S = Sindroma(mens)
correcaoErro = correccaoDoErro(S,mens,retirabits[1])
resize_CDE = arrayDeCod(correcaoErro,nBits)
arrayDescodificado = binTOint(resize_CDE,nBits)
desq = lambda x : TabelasQuantizacao[arrayDescodificado]
desq = desq(arrayDescodificado)
BER = np.sum(((retirabits[0] + filtro)%2)/len(retirabits[0]))
BERL = np.sum(((ib8 + correcaoErro)%2))/len(ib8)

##sem modulo de correção de erros
ASK_SCE = sinalASK(ib8,P,A1,A0)
canalAWGN_SCE = canal_AWGN(ASK_SCE,pot)
filtro_SCE = filtroASK(canalAWGN_SCE,A1,A0,P)
resize_SCE = arrayDeCod(filtro_SCE,nBits)
arrayDescodificado_SCE = binTOint(resize_SCE,nBits)
desq_SCE = lambda x : TabelasQuantizacao[arrayDescodificado_SCE]
desq_SCE = desq_SCE(arrayDescodificado)
BER_SCE = np.sum(((ib8 + filtro_SCE)%2))/len(ib8)

if __name__ == "__main__":
    erro = erroQ(data,nBits)
    erro8 = desq - data
    erro8_SCE = desq_SCE - data
    SNR_I = SNRP(erro,data)
    SNR_F = SNRP(erro8,data)
    SNR_F_SCE = SNRP(erro8_SCE,data)
    print("BERS")
    print(BER)
    print(BERL)
    print(BER_SCE)
    print("SNR")
    print(SNR_I)
    print(SNR_F)
    print(SNR_F_SCE)
    wav.write("sound/ex4_grupo_B.wav",sampleRate,desq.astype('int16'))
    wav.write("sound/ex4_grupo_B_SCE.wav",sampleRate,desq_SCE.astype('int16'))
    plt.plot(desq)
    plt.plot(vq)
    plt.show()
    plt.plot(desq_SCE)
    plt.plot(vq)
    plt.show()
    
