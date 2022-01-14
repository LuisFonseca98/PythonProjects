import matplotlib.pyplot as plt
import numpy as np

nI=[-50,50]
n=np.arange(nI[0], nI[1]+1 ,1)
x=(10/(np.pi*n))*np.sin((np.pi*n)/10)
x[50]=1
#configurações do plot
plt.close('all')
plt.figure(facecolor='grey',figsize=(18,8))

plt.stem(n,x,'k',linewidth=1.5)

plt.xlabel('$n$');
plt.ylabel('$x$');   
plt.grid('on')
plt.title("Exercicio 4 - alinea b)", fontsize = 20)
plt.show()
