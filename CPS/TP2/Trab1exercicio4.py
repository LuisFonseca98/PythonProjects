import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy import signal

def leiA(A,rampa):
    m = 2*(rampa - np.min(rampa))/np.ptp(rampa)-1 

    lei = np.piecewise(m,[np.abs(m) >= 1/A, np.abs(m) <= 1/A],\
                       [lambda x : np.sign(x)*(1+np.log(A * np.abs(x)))/(1 + np.log(A)),\
                        lambda y: ((A)/(1 + np.log(A))) * y  ] )

    return lei

