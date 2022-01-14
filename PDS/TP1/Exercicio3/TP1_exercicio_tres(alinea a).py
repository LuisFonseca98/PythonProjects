import numpy as np
from matplotlib import pyplot as plt

def soma(f0,t,N):
    x = np.zeros(t.shape)
    for k in np.arange(1,N+1):
        x = x + np.sin(2*np.pi*(2.*k-1)*f0*t)/(2.*k-1)
    x = x*4/np.pi
    return x

Ns = [1,10,10000]
plt.figure(facecolor = 'grey', figsize = (18,8))
m = 1
f0= 1
n_periodos = 6.0
tI=[0.0,n_periodos/f0]
t = np.linspace(tI[0],tI[1],1e4)
for i in Ns:
    N = i
    x = soma(f0,t,N)
    plt.subplot(3,1,m)
    plt.plot(t,x,"k",linewidth=2)
    h_tick = (tI[1]-tI[0])/5.
    v_tick = (np.max(x) - np.min(x))/4.
    plt.xticks(np.arange(tI[0],tI[1] + h_tick,h_tick), fontsize = 10)
    plt.yticks(fontsize = 10)
    m = m + 1
plt.text(3.05, 6.8, "Exeercicio 3 - alinea a)", horizontalalignment='center', fontsize=20)
plt.show()
        
