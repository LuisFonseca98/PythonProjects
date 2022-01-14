from matplotlib import pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
print("-- Reconhecimento de notas e seu tempo, a partir de ficheiro wav --")
#Ler sinal wav
sinal = wav.read('Musica.wav')
#print(sinal)

#specgram[espectro,frequencia,tempo]
s = plt.specgram(sinal[1],NFFT=512, Fs=sinal[0])
espectro, f, t, img = plt.specgram(sinal[1],NFFT=1024, Fs=sinal[0])
#plt.show()
#print(s)

#Lista de x maximos
lista=[]
lista2=[]
for j in np.arange(0,espectro.shape[1],1):
    plt.plot(f,espectro[:,j])
    lista.append(np.argmax(espectro[:,j]))
#print(lista)
#print(f[lista])

total = 0
#Lista de x no pontos maximos
for i in range(len(lista)-1):
    if(lista[i] != lista[i+1]):
        lista2.append((lista[i],round(t[i])-total))
        total = round(t[i])
lista2.append((lista[len(lista)-1],round(t[i])-total))
print("2-Ponto x dos valores maximos: "+str(lista2))

#Lista das frequencias correspondentes aos x maximos
lista3=[]
for i in lista2:
    lista3.append((f[i[0]],i[1]))
print("3-Frequencias correspondentes aos maximos: "+str(lista3))

#Frequencia correta
lista4=[]
fNotas=2**(np.arange(12*3.)/12.)*260
for i in lista3:
    freq = np.argmin(np.abs(fNotas-i[0]))
    lista4.append((fNotas[freq],i[1]))
print("4-Frequencias e tempo final: "+str(lista4))

#Valor do N para ca da frequencia
lista5=[]
for i in lista4:
    N=np.log2(i[0]/440)*12+49
    lista5.append((round(N),i[1]))
print("5-Numero da nota e o respetivo tempo: "+str(lista5))

#Dicionario de notas
dicionario_notas = {40 :'c' , 44 : 'e', 47 : 'g', 52 : 'c5'}

#Composicao de notas finais
lista6=[]
for nota in lista5:
    X=dicionario_notas[nota[0]]
    lista6.append((X,nota[1]))
print("6-Composicao de notas finais"+str(lista6))
