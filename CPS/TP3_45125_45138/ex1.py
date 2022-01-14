import numpy as np
import matplotlib.pyplot as plt

def manch(P,A,n):
    n = n.flatten()
    resultado = map(lambda x : np.hstack((np.ones(int(P/2)) * A , np.ones(int(P/2)) * -A)) if( n[x] == 0 )
               else np.hstack((np.ones(int(P/2)) * -A , np.ones(int(P/2)) * A )),range(len(n)))
    resultado = np.array(list(resultado))
    return resultado.flatten()

