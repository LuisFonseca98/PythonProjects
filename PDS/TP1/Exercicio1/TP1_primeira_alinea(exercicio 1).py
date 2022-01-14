import numpy as np
from matplotlib import pyplot as plt
#primeira alinea com o intervalo [-1,3]
tMin = -1
tMax = 3
t = np.arange(tMin, tMax, 0.000001)
x1 = 2*np.cos(2*np.pi*10*t + np.pi/4) + np.sin(2*np.pi*11*t - np.pi/3)
plt.close('all')
plt.figure(facecolor = 'grey', figsize = (18,8))
plt.plot(t,x1,'k',lw=3)
plt.grid()
plt.axis([tMin,tMax,0,1])
plt.xticks(np.arange(-1,3.1,0.5),fontsize=20)
plt.yticks(np.arange(-3,3.5,0.5),fontsize=20)
plt.xlabel("t(s)",fontsize=30)
plt.ylabel("y",fontsize=30)
plt.text(.50,3.5,"Funcao da alinea a)",fontsize=15)
plt.text(.50,3.1,r'$x(t)={2cos(2{\pi}10t + \frac{\pi}{4}}) + {sin(2{\pi}11t - \frac{\pi}{3})}$',fontsize=15)
plt.show()
