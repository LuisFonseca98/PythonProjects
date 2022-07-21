from mod.estado import Estado

"""
Classe que representa o estado localidade
"""

class EstadoLocalidade(Estado):

    """
    Construtor que inicializa a localidade (inicial e final)
    """
    def __init__(self, localidade):
        self._localidade = localidade

    def id_valor(self):
        return self._localidade.__hash__()

    @property
    def localidade(self):
        return self._localidade

