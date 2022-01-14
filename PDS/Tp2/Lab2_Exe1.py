import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def sinal(f,d,Fs):
    t = np.arange(0,d,1/Fs)
    x = 2*np.cos(2*np.pi*f*t)
    return x

Fs = 1000.0

f=((43789+43789)/(2*100))

s = sinal(f,1 ,Fs)
wav.write('teste1.wav',Fs,s.astype('int16'))

#dominio do tempo
plt.figure()
plt.plot(s)
#
# #dominio da frequencia
X = np.fft.fft(s)
freqs = np.fft.fftfreq(len(X),1./Fs)
plt.axis([0,438,0,2])
plt.plot(freqs)
#
# # #dominio da amplitude
plt.figure()
plt.plot(np.abs(X))
#
# #
plt.figure()
plt.plot(np.angle(X))
# #
plt.figure()
plt.specgram(s, Fs = Fs)
plt.show()
