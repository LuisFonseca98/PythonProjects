from random import choice

from ecr.comportamento import Comportamento
from sae import Direccao

from ..resposta.resposta_mover import RespostaMover

"""
Classe que representa o comportamento explorar
"""

class Explorar(Comportamento):
    def activar(self, percepcao):
        direccao = choice(list(Direccao)) #escolhe uma direcao aletatoria
        resposta = RespostaMover(direccao) #o agente move-se consoante essa resposta
        return resposta.activar(percepcao) #ativa essa resposta 
