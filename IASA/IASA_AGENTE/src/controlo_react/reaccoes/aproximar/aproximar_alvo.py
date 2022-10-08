from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao
from .aproximar_dir import AproximarDir


"""
Classe que representa o comportamento aproximar alvo
"""
class AproximarAlvo(Prioridade):
    """
    Aproxima-se duma direccao consoante o alvo
    """
    def __init__(self):
        super().__init__([
            AproximarDir(direccao) for direccao in Direccao
        ])
