import numpy as np
from matplotlib import pyplot as plt

yMax = 1
yMin = -1
tI=[-2.005,-1.505]
t=np.linspace(tI[0],tI[1],1e4)

u1=np.zeros(t.shape)
u2=np.zeros(t.shape)
u1[(t>=-2)]=1
u2[(t>=-1.53)]=1
x2 = np.cos(2*np.pi*15*t)
x1 = x2*(u1-u2)
plt.close('all')
plt.figure(facecolor = 'gray',figsize = (20,16))
plt.plot(t,x1,lw=3)
plt.grid()
plt.axis([tI[0],tI[1],yMin,yMax])
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel("t(s)",fontsize =15)
plt.ylabel("y",fontsize =15)
plt.title("Exercicio 2 - alinea b)", fontsize = 20)
plt.show()

