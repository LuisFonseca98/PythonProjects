

from ecr.reaccao import Reaccao

from .estimulo_obst import EstimuloObst

"""
Classe que permite evitar um obstaculo, consoante uma direcao
"""
class EvitarDir(Reaccao):
    def __init__(self, direccao, resposta):
        super().__init__(
            EstimuloObst(direccao),
            resposta
        )
