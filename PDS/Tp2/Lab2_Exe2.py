import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
#1 Parsing
#2 Frequencia de cada nota
#3 Geracao
#4 Concatenacao
#5 Gravacao
#plt.figure()

def musica(notas):
    musica=[]
    for nota in notas:
        N = dicionario_notas[nota[0]]
        Fn=2**((N-49)/12.0)*440
        t=np.arange(0,nota[1],1.0/16000)
        x=20000*np.cos(2*np.pi*Fn*t)
        musica=np.hstack((musica,x))
        print(Fn)
        print(x)
        print(t)
        print(musica)
    return musica

notas=[('c', 4), ('e', 4), ('g', 4), ('c5', 1)]
dicionario_notas = {'c' : 40, 'e' : 44, 'g' : 47, 'c5' : 52}

#Fn=2*((N-49)/12)*440
#t=np.arange(0,d,1./Fn)
#x=A*np.cos(2*np.pi*Fn*t)

musica=musica(notas)
#plt.plot(t, x)
wav.write('Musica.wav',16000,musica.astype('int16'))


d=3
pAttack=0.1
pDecay=0.05
pSustain=0.85
pRelease=0.05
Fs=10000
t=np.zeros(d*Fs)
adsr=np.zeros(d*Fs)
t=np.arange(0, d*pAttack, 1./Fs)
adsr[0:len(t)]=1./(d*pAttack)*t
plt.plot(adsr)

t=np.arange(d*pAttack, d*(pAttack+pDecay), 1./Fs)
adsr[int(d*pAttack*Fs):int(d*(pAttack+pDecay))]=1.
plt.plot(adsr)

t=np.arange(d*(pAttack+pDecay), d*(pAttack+pDecay+pSustain), 1./Fs)
adsr[int(d*(pAttack+pDecay)*Fs):int(d*(pAttack+pDecay+pSustain))]=1.
plt.plot(adsr)

t=np.arange(1, d*pRelease, 1./Fs)
adsr[int(d*(pAttack+pDecay+pSustain))*Fs:d*Fs]=6.-(6./(pRelease*d))*t
plt.plot(adsr)


plt.show()
