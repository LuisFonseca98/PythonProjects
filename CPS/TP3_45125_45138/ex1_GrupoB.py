import numpy as np
import matplotlib.pyplot as plt 


def sinalASK(n,P,A1,A0):
    N = P
    s0 = np.cos(2 * np.pi * (np.arange(P)/N))
    ASK = map(lambda x: A1 * s0 if(x == 1) else A0 * s0,n)
    return np.array(list(ASK)).flatten()


