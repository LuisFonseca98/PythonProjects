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

sampleRate,data = wav.read("sound/CPS_Exercicio1.wav")
data = np.array(data[:,0],'int16')
##sampleRate,data = wav.read("sound/bM.wav")
##data = np.array(data,'int16')
P = 8
A1 = 2
A0 = 1
nBits = 8

sinal,vq,TabelasQuantizacao = quantizacao(data,nBits)
ib8 = intTObin(sinal,nBits)
hamming = hamming74(ib8)
retirabits = retiraBitsAdicionados(hamming)
ASK = sinalASK(retirabits[0],P,A1,A0)
canalAWGN = canal_AWGN(ASK,0.012)
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
if __name__ == "__main__":
    print("BERS")
    print(BERL)
    print(BER)
    wav.write("sound/ex3_grupo_B.wav",sampleRate,desq.astype('int16'))
    plt.plot(desq)
    plt.plot(vq)
    plt.show()
