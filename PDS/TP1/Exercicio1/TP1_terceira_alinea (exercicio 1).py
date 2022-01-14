import numpy as np
from matplotlib import pyplot as plt
#intervalo entre [31,33]
tMax = 33
tMin = 31
yMax = 1
yMin = -1
t = np.arange(tMin,tMax,10./1000)#arange(início, fim, intervalo
x1 = (1/3+2/3*np.cos(5*np.pi*t))*np.cos(100*np.pi*t)
plt.close('all')
plt.figure(facecolor = 'gray',figsize = (20,16))
plt.plot(t,x1,lw=3)
plt.grid()
plt.axis([tMin,tMax,yMin,yMax])
plt.xticks(np.arange(tMin,tMax,.5),fontsize=30)
plt.yticks(np.arange(yMin,yMax,.5),fontsize=30)
plt.ylabel("y",fontsize =15)
plt.xlabel("t(s)",fontsize =15)
plt.text(31.8,1.15,"Funcao da alinea c)",fontsize=15)
plt.text(31.8,1.05,r'$x(t)={\frac{1}{3} + \frac{2}{3}cos(5{\pi}t)cos(100{\pi}t})$',fontsize=15)
plt.show()
