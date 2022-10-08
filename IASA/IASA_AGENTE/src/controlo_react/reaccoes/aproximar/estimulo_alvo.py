from ecr.estimulo import Estimulo
from sae import Elemento


"""
Classe que representa o estimulo alvo
"""
class EstimuloAlvo(Estimulo):

    """
    Construtor que recebe a direcao e um gama: valor que tem de ser inversamente proporcional
    """
    def __init__(self, direccao, gama=0.9):
        self._gama = gama
        self._direccao = direccao

    """
    Método que deteta um alvo
    Consoante o alvo deteta, aumenta o valor da gama
    """
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self._direccao]
        if elemento == Elemento.ALVO:
            return self._gama ** distancia
        else:
            return 0
