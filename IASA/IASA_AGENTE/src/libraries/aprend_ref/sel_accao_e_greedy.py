import random
from aprend_ref.sel_accao import SelAccao

"""
Classe que representa a seleccao da accao segundo a estrategia greedy
"""
class SelAccaoEGreedy(SelAccao):

    def __init__(self,mem_aprend,accoes,epsilon):
        self._mem_aprend = mem_aprend
        self._accoes = accoes
        self._epsilon = epsilon

    """
    Metodo que permite ao agente escolher se vai explorar ou aproveitar(accao sofrega)
    """
    def seleccionar_accao(self, s):
        randomChoice = random.random()
        accao = None
        if randomChoice < self._epsilon:
            accao = self.explorar()
        else:
            accao = self.accao_sofrega(s)
        return accao

    """
    Metodo que retorna a accao que maximiza o valor de q
    """
    def accao_sofrega(self,s):
        random.shuffle(self._accoes)
        return max(self._accoes, key=lambda a: self._mem_aprend.q(s, a))
        
    """
    Metodo onde o agente vai explorar, fazendo um random com das diferentes accoes
    """
    def explorar(self):
        accoes = random.choice(self._accoes)
        return accoes
