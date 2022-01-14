
import matplotlib.pyplot as plt
import numpy as np

nI=[0,32]
n=np.arange(nI[0], nI[1]+1 ,1)
x=np.cos((2*np.pi)*(n/16))

#configurações do plot
plt.close('all')
plt.figure(facecolor='grey',figsize=(18,8))

plt.stem(n,x,'k',linewidth=1.5)

plt.xlabel('$n$');
plt.ylabel('$x$');
plt.xticks(range(-1,34))    
plt.grid('on')
plt.title("Exercicio 4 - alinea a)",fontsize = 20)
plt.show()
