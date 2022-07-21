from ecr.hierarquia import Hierarquia
from sae import Direccao

from .evitar_dir import EvitarDir
from .resposta_evitar import RespostaEvitar

"""
Classe que representa o agente evitar o obstaculo que encontra a sua frente
"""
class EvitarObst(Hierarquia):
    def __init__(self):
        self._resposta = RespostaEvitar()
        super().__init__([
            EvitarDir(direccao, self._resposta) for direccao in Direccao
        ])
