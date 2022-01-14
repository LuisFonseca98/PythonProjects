import numpy as np

def filtroASK(sinal,A1,A0,P):
    N = P
    b = np.sqrt(2/P) * np.cos(2*np.pi * (np.arange(P)/N))
    s0 = A0 * np.cos(2 * np.pi * (np.arange(P)/N))
    s1 = A1 * np.cos(2 * np.pi * (np.arange(P)/N))
    E0 = np.sqrt(np.sum(s0**2))
    E1 = np.sqrt(np.sum(s1**2))
    limDecisao = ((E1) + (E0))/4
    copiaSinal = sinal.copy()
    copiaSinal.resize(((int)(len(sinal)/P),P))
    resFinal = np.array(list(map(lambda x: 1 if(((copiaSinal[x][0])>=limDecisao
                                                 and copiaSinal[x][4]*-1>=limDecisao))
                                 else 0,range(len(copiaSinal)))))
    return resFinal
