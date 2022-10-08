

"""
Classe que corresponde a distancia heuristica
"""
from math import dist
from pee.melhor_prim.heuristica import Heuristica


class HeurDist(Heuristica):

    """
    Construtor da classe, necessitando de conhecer o estado final
    """
    def __init__(self,estado_final):
        self._estado_final = estado_final

    """
    Metodo que calcula a distancia heuristica
    Fazendo a distancia euclidade entre dois pontos(neste caso o estado e o estado final)
    """
    def h(self, estado):
        return dist(estado.posicao,self._estado_final.posicao)