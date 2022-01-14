import matplotlib.pyplot as plt
import numpy as np

nI=[-15,15]
n=np.arange(nI[0], nI[1]+1 ,1)
x=np.exp(-np.absolute(n/3))*np.cos(2*np.pi*(np.pi/2))
#configurações do plot
plt.close('all')
plt.figure(facecolor='grey',figsize=(18,8))

plt.stem(n,x,'k',linewidth=1.5)
plt.xlabel('$n$');
plt.ylabel('$x$');   
plt.grid('on')
plt.title("Exercicio 4 - alinea c)", fontsize = 20)
plt.show()
