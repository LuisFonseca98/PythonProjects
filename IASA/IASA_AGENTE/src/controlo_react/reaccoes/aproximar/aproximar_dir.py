from ecr.reaccao import Reaccao

from ..resposta.resposta_mover import RespostaMover
from .estimulo_alvo import EstimuloAlvo


"""
Classe que representa o comportamento aproximar dir
"""

class AproximarDir(Reaccao):

    """
    Construtor onde consoante a direcao que se aproxima, recebe um estimulo(alvo) e a resposta (mover)
    """
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao),
            RespostaMover(direccao))
