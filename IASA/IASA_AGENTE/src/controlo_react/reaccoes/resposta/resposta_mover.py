from ecr.resposta import Resposta
from sae import Accao

"""Classe que representa a resposta mover(accao)"""

class RespostaMover(Resposta):
    def __init__(self, direccao):
        super().__init__(Accao(direccao))
