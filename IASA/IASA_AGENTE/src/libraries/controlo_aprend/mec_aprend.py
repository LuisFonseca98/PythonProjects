

from aprend_ref.aprend_q import AprendQ
from aprend_ref.memoria_esparsa import MemoriaEsparsa
from aprend_ref.sel_accao_e_greedy import SelAccaoEGreedy

"""
Classe que representa o controlo de aprendizagem
"""
class MecAprend:

    """
    Constutor que inicializa um conjunto de accoes
    obtem o conjunto de estados
    inicializa a memoria em esparsa
    seleciona a accao consoante a estrategia greedy
    inicializa a aprendizagem com o algoritmo Q-learning
    """
    def __init__(self,accoes,alfa = 0.5,gama = 0.9,epsilon = 0.01):
        self._accoes = accoes
        self._mem_aprend = MemoriaEsparsa()
        self._estados = self._mem_aprend.obter_estados()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend,self._accoes,epsilon)
        self._aprend_ref = AprendQ(self._mem_aprend,self._sel_accao,alfa,gama)
        
    """
    Metodo que aprende por aprendizagem por reforco
    """
    def aprender(self,s,a,r,sn):
        self._aprend_ref.aprender(s,a,r,sn)

    """
    Metodo que seleciona uma accao
    """
    def selecionar_accao(self,s):
        return self._sel_accao.seleccionar_accao(s)

    """
    Metodo que seleciona uma accao sofrega
    """
    def accao_sofrega(self,s):
        return self._sel_accao.accao_sofrega(s)

    """
    Metodo que inicializa o algoritmo q-learning
    """
    def q(self,s,a):
        return self._mem_aprend.q(s,a)

    @property
    def estados(self):
        return self._estados
