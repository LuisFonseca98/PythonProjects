
"""
Representa o estado do agente
"""
from mod.estado import Estado


class EstadoAgente(Estado):

    """
    Construtor que inicializa a posicao do agente
    """
    def __init__(self,posicao):
        self._posicao = posicao

    """
    Metodo que referencia a posicao do agente
    """
    def id_valor(self):
        return self.posicao.__hash__()

    @property
    def posicao(self):
        return self._posicao