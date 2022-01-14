import numpy as np
from ex1 import *


def canal_AWGN(sinal_in, pot):
    sinal_out = sinal_in + np.sqrt(pot)*np.random.randn(1, len(sinal_in))
    return sinal_out.flatten()

