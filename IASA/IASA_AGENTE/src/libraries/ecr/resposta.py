
"""
Classe  que representa a resposta do agente
"""
class Resposta:

    """
    Construtor que conhece a accao (resposta)
    """
    def __init__(self, accao):
        self._accao = accao

    """
    Metodo que activa uma percepcao baseada na intensidade
    """

    def activar(self, percepcao, intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao
