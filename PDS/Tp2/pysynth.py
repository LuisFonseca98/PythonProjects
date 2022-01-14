import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
import pysynth as ps

notas = (('c' , 4) , ('e', 4) , ('g', 4) , ('c5', 1))
ps.make_wav(notas, fn = "teste_pysynth.wav")

