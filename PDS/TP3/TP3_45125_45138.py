import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
Fs,som = wav.read('cartoon001.wav')
Fs2,som2 = wav.read('Musica.wav')

#----------------------------alinea a)-------------------------
#-------------------------------------Y1----------------------------
#--------Y1 c = 1 r =-0.9----------
plt.figure()
ak1 = [1.]
bk1 = [1.,-0.9]
plt.subplot(3,1,1)
w,h = ss.freqz(bk1,ak1)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] + 0.9x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y1 c = 1 r =0.1----------
ak2 = [1.]
bk2 = [1.,0.1]
plt.subplot(3,1,2)
w,h = ss.freqz(bk2,ak2)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] - 0.1x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y1 c = 1 r =0.9----------
ak3 = [1.]
bk3 = [1.,0.9]
plt.subplot(3,1,3)
w,h = ss.freqz(bk3,ak3)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] - 0.9x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))
plt.show()

#--------Y1 c = 2 r =-0.9----------
plt.figure()
ak4 = [1.]
bk4 = [1.,0.,-0.9]
plt.subplot(3,1,1)
w,h = ss.freqz(bk4,ak4)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] + 0.9x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y1 c = 2 r =0.1----------
ak5 = [1.]
bk5 = [1.,0.,0.1]
plt.subplot(3,1,2)
w,h = ss.freqz(bk5,ak5)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] - 0.1x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y1 c = 2 r =0.9----------
ak6 = [1.]
bk6 = [1.,0.,0.9]
plt.subplot(3,1,3)
w,h = ss.freqz(bk6,ak6)
plt.grid()
plt.title("alinea a) Filtro y1[n] = x[n] - 0.9x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))
plt.show()

#--------------------------------------Y2---------------------------
#--------Y2 c = 1 r =-0.9----------
plt.figure()
ak7 = [1.,-0.9]
bk7 = [1.]
plt.subplot(3,1,1)
w,h = ss.freqz(bk7,ak7)
plt.grid()
plt.title("alinea a) Filtro y2[n] = x[n] + 0.9y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y2 c = 1 r =0.1----------
ak8 = [1.,0.1]
bk8 = [1.]
plt.subplot(3,1,2)
w,h = ss.freqz(bk8,ak8)
plt.grid()
plt.title("alinea a) Filtro y2[n] = x[n] - 0.1y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y2 c = 1 r =0.9----------
ak9 = [1.,0.9]
bk9 = [1.]
plt.subplot(3,1,3)
w,h = ss.freqz(bk9,ak9)
plt.grid()
plt.plot(w,np.abs(h))
plt.title("alinea a) Filtro y2[n] = x[n] - 0.9y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.show()

#--------Y2 c = 2 r =-0.9----------
plt.figure()
ak10 = [1.,0.,-0.9]
bk10 = [1.]
plt.subplot(3,1,1)
w,h = ss.freqz(bk10,ak10)
plt.grid()
plt.title("alinea a) Filtro y2[n] = x[n] + 0.9y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))

#--------Y2 c = 2 r =0.1----------
ak11 = [1.,0.,0.1]
bk11 = [1.]
plt.subplot(3,1,2)
w,h = ss.freqz(bk11,ak11)
plt.grid()
plt.title("alinea a) Filtro y2[n] = x[n] - 0.1y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(w,np.abs(h))
#--------Y2 c = 2 r =0.9----------
ak12 = [1.,0.,0.9]
bk12 = [1.]
plt.subplot(3,1,3)
w,h = ss.freqz(bk12,ak12)
plt.grid()
plt.plot(w,np.abs(h))
plt.title("alinea a) Filtro y2[n] = x[n] - 0.9y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.show()

#----------------------------alinea c)-------------------------
t = np.arange(-5,5,1./1000)

x = 10 + 2*np.cos((np.pi/6)*t)+10*np.cos((np.pi/3)*t)

#----Y1--c =1 R = -0.9--------------------------------------
plt.figure()
y = ss.lfilter(bk1,ak1,x)
plt.subplot(3,1,1)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] + 0.9x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
#----Y1--c =1 R = 0.1--------------------------------------
y = ss.lfilter(bk2,ak2,x)
plt.subplot(3,1,2)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] - 0.1x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
#----Y1--c =1R = 0.9 ---------------------------------
y = ss.lfilter(bk3,ak3,x)
plt.subplot(3,1,3)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] - 0.9x[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
plt.show()
#----Y1--c =2 R = -0.9--------------------------------------
plt.figure()
y = ss.lfilter(bk4,ak4,x)
plt.subplot(3,1,1)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] + 0.9x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
#----Y1--c =2 R = 0.1--------------------------------------
y = ss.lfilter(bk5,ak5,x)
plt.subplot(3,1,2)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] - 0.1x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
#----Y1--c =2 R = 0.9 ---------------------------------
y = ss.lfilter(bk6,ak6,x)
plt.subplot(3,1,3)
plt.grid()
plt.title("alinea c) Filtro y1[n] = x[n] - 0.9x[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
plt.show()

#----Y2--c=1 R = -0.9 -----------------------------
plt.figure()
y = ss.lfilter(bk7,ak7,x)
plt.subplot(3,1,1)
plt.title("alinea c) Filtro y2[n] = x[n] + 0.9y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.grid()
plt.plot(t,y)
#----Y2--c =1 R = 0.1--------------------------------------
y = ss.lfilter(bk8,ak8,x)
plt.subplot(3,1,2)
plt.grid()
plt.title("alinea c) Filtro y2[n] = x[n] - 0.1y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)

#----Y2--c =1 R = 0.9 ---------------------------------
y = ss.lfilter(bk9,ak9,x)
plt.subplot(3,1,3)
plt.grid()
plt.title("alinea c) Filtro y2[n] = x[n] - 0.9y2[n-1]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
plt.show()

#----Y2--c =2 R =-0.9 ---------------------------------
plt.figure()
y = ss.lfilter(bk10,ak10,x)
plt.subplot(3,1,1)
plt.grid()
plt.title("alinea c) Filtro y2[n] = x[n] + 0.9y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)

#----Y2--c =2 R = 0.1--------------------------------------
y = ss.lfilter(bk11,ak11,x)
plt.subplot(3,1,2)
plt.grid()
plt.title("alinea c) Filtro y2[n] = x[n] - 0.1y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)

#----Y2--c =2 R = 0.9 ---------------------------------
y = ss.lfilter(bk12,ak12,x)
plt.subplot(3,1,3)
plt.grid()
plt.title("alinea c) Filtro y2[n] = x[n] - 0.9y2[n-2]")
plt.subplots_adjust(hspace = 0.75)
plt.plot(t,y)
plt.show()

plt.figure()


###Para o segundo grupo:
###ss.firwin(numtaps(numero de atrasos), cutoffs(frequencia de corte), pass_zero (boolean),nyq=fyq)
###atraves do firwin, constroi-se um sistema fir, nao precisa de calcular o ak, pois o valor dele vai ser 1(ak = 1)
###pass- deixa passar a frequencia maior que zero(quando e true), e faso quando a frequencia e menor que 0
###PassaBaixo - ss.firwin(numtaps,cutoffs, pass_zero = true, nyq = Fs/2)
###PassaBanda - ss.firwin(numtaps,[fc1,fc2], pass_zero = false,nyq = Fs/2)
###PassaAlto - ss.firwin(numtaps,fc,zero_pass= False,nyq = Fs/2)
###nyq e opcional, por isso se nao for posto, o cut_off tem de estar num array entre 0 e 1, ou seja [0,1]  que corresponde a [0,pi] ou [0,Fs/2]
###Fs = 1000.0
###exemplo:ss.firwin(numtaos,[0,Fs/2],pass_zero)
###exemplo2: ss.firwin(11,100.0,pass_zero = true,nyq = 500)
###exemplo3: ss.firwin(11,1./5,pass_zero = true,nyq = 500)
####w,h = ss.freqz(bk,[1.0])
####plt.plot(w,np.abs(h))
####plt.show
##
Fs = 1000.0
#a) filtro passa-baixo
bka = ss.firwin(1001, (Fs/2.)/3., pass_zero = True, nyq = Fs/2.0)
w,h = ss.freqz(bka, [1.0])
plt.subplot(311)
plt.subplots_adjust(hspace = 0.5)
plt.title("Filtro passa-baixo")
plt.plot(w / np.pi * Fs/2.0, np.abs(h))

#b) filtro  passa-alto
bkb = ss.firwin(1001, (Fs/2.)/3., pass_zero = False, nyq = Fs/2.0)
w,h = ss.freqz(bkb, [1.0])
plt.subplot(312)
plt.subplots_adjust(hspace = 0.5)
plt.title("Filtro passa-alto")
plt.plot(w / np.pi * Fs/2.0, np.abs(h))

#c) filtro passa-banda entre pi/4 e pi/3
bkc = ss.firwin(1001,[(Fs/2.)/4.,(Fs/2.)/3.], pass_zero = False, nyq = Fs/2.0)
w,h = ss.freqz(bkc, [1.0])
plt.subplot(313)
plt.subplots_adjust(hspace = 0.5)
plt.title("Filtro passa-banda")
plt.plot(w / np.pi * Fs/2.0, np.abs(h))
plt.show()

#d) wav's dos filtros  WIP
plt.figure()
ak = [1.0]
#-------------filtro a) do wav Fs,som------------------------
ya = ss.lfilter(bka,ak,som)
plt.subplot(3,1,1)
plt.title("Resultado quando aplicado o ficheiro wav cartoon001")
plt.subplots_adjust(hspace = 0.5)
plt.plot(ya)


#-------------filtro b) do wav Fs,som ------------------------
yb = ss.lfilter(bkb,ak,som)
plt.subplot(3,1,2)
plt.title("Resultado quando aplicado o ficheiro wav cartoon001")
plt.subplots_adjust(hspace = 0.5)
plt.plot(yb)


#-------------filtro c)do wav Fs,som ------------------------
yc = ss.lfilter(bkc,ak,som)
plt.subplot(3,1,3)
plt.title("Resultado quando aplicado o ficheiro wav cartoon001")
plt.subplots_adjust(hspace = 0.75)
plt.plot(yc)
plt.show()

#-------------filtro a) do wav Fs2,som2------------------------
ya2 = ss.lfilter(bka,ak,som2)
plt.subplot(3,1,1)
plt.title("Resultado quando aplicado o ficheiro wav Musica")
plt.subplots_adjust(hspace = 0.75)
plt.plot(ya2)
#-------------filtro b) do wav Fs2,som2------------------------
yb2 = ss.lfilter(bkb,ak,som2)
plt.subplot(3,1,2)
plt.title("Resultado quando aplicado o ficheiro wav Musica")
plt.subplots_adjust(hspace = 0.75)
plt.plot(yb2)
#-------------filtro c) do wav Fs2,som2------------------------
yc2 = ss.lfilter(bkc,ak,som2)
plt.subplot(3,1,3)
plt.title("Resultado quando aplicado o ficheiro wav Musica")
plt.subplots_adjust(hspace = 0.75)
plt.plot(yc2)
plt.show()


