
import numpy as np
from matplotlib import pyplot as plt
#intervalo entre [-2,2]
tMax = 123
tMin = 121
yMax = 2
yMin = -2
t = np.arange(tMin,tMax,10./1000)#arange(início, fim, intervalo
x1 = np.cos(540*np.pi*t+np.pi/2)+np.cos(545*np.pi*t-np.pi/2)
plt.close('all')
plt.figure(facecolor = 'gray',figsize = (18,8))
plt.plot(t,x1,lw=3)
plt.grid()
plt.axis([tMin,tMax,yMin,yMax])
plt.xticks(np.arange(tMin,tMax,.5),fontsize=30)
plt.yticks(np.arange(yMin,yMax,.5),fontsize=30)
plt.xlabel("t(s)",fontsize =15)
plt.ylabel("y",fontsize =15)
plt.text(121.7,2.30,"Funcao da alinea b)",fontsize=15)
plt.text(121.7,2.10,r'$x(t)={cos(540{\pi}t +\frac{\pi}{2}}) + {cos(545{\pi}t + \frac{\pi}{2})}$',fontsize=15)
plt.show()
