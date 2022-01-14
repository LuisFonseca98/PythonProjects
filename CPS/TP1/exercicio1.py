import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from scipy import signal as sg


#alinea a)
nPontos = 4096
FsAmost = 8000
tI = [0,1]
t1=np.arange(tI[0],tI[1],1.0/FsAmost)

#Sinal original
x = 20000*np.cos(2*np.pi*3014*t1)
wav.write("sound/sinalOriginal.wav",FsAmost,np.int16(x))
xfft = np.fft.fft(x[0:nPontos])
freq = np.fft.fftfreq(len(xfft)) * FsAmost
a = np.abs(xfft) / nPontos
#soundPlay(x,FsAmost)

#Sinal Amostrado
xAmostrado = x[0:len(x) + 1:2]
novaFsAmost = 4000
t2 = np.arange(tI[0],tI[1], 1.0/novaFsAmost)
wav.write("sound/sinalAmostrado.wav",novaFsAmost,np.int16(xAmostrado))
xfft2 = np.fft.fft(xAmostrado[0:nPontos])
freq2 = np.fft.fftfreq(len(xfft2)) * novaFsAmost
a2 = np.abs(xfft2) / nPontos

####plotSinalOriginal
plt.close('all')
plt.figure(facecolor='w',figsize=(18,8))
plt.xlabel("f(Hz)",fontsize = 20)
plt.ylabel("Amplitude",fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig("img/exercicio1_sinalOriginal(EspetroFrequencia).png")
plt.plot(freq,a,'k',linewidth=1.5)#Represetacao do espetro da frequencia com parametro a e freq
plt.plot(freq,np.angle(xfft),'k',linewidth=1.5) #Representacao do espetro da amplitude com parametro fase e freq
plt.grid()

##plotSinalAmostrado
plt.figure(facecolor='w',figsize=(18,8))
plt.plot(freq2,a2,'k',linewidth=1.5)#Represetacao do espetro da frequencia com parametro a e freq
plt.plot(freq,np.angle(xfft),'k',linewidth=1.5) #Representacao do espetro da amplitude com parametro fase e freq
plt.xlabel("f(Hz)",fontsize = 20)
plt.ylabel("Amplitude",fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig("img/exercicio1_sinalAmostrado(EspetroFrequencia).png")
plt.grid()
plt.show()
#-----------------------------------------------------------------------------

#alinea b)
#sinalAudio
sampleRate,data=wav.read("sound/CPS_Exercicio1.wav")
data = np.array(data[:,0],'float32')
xfft3 = np.fft.fft(data)
freq3 = np.fft.fftfreq(len(xfft3)) * sampleRate
a3 = np.abs(xfft3) / nPontos

#sinalAudioAmostrado
novaFsAmost2 = 1000
dataAmostrado = sg.resample(data,novaFsAmost2)
xfft4 = np.fft.fft(data)
freq4 = np.fft.fftfreq(len(xfft4)) * novaFsAmost2
a4 = np.abs(xfft4) / nPontos

plt.close('all')
plt.figure(facecolor='w',figsize=(18,8))
plt.xlabel("f(Hz)",fontsize = 20)
plt.ylabel("Amplitude",fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig("img/sinalAudioOriginal(EspetroFrequencia).png")
plt.plot(freq3,a3,'k',linewidth=1.5)
plt.grid()
plt.show()

plt.figure(facecolor='w',figsize=(18,8))
plt.xlabel("f(Hz)",fontsize = 20)
plt.ylabel("Amplitude",fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig("img/sinalAudioOriginalAmostrado(EspetroFrequencia).png")
plt.plot(freq4,a4,'k',linewidth=1.5)
plt.grid()
plt.show()
wav.write("sound/sinalAudioAmostrado.wav",novaFsAmost2,np.int16(dataAmostrado))

