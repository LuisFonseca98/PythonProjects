from abc import ABC, abstractmethod

"""
Classe que representa a fronteira de exploracao
"""
class Fronteira(ABC):

    """
    Construtor que inicializa a lista de nos
    """
    def __init__(self):
        self._nos = list()
 
    """
    Metodo que retorna true, onde verifica se a lista de nos esta vazia
    """
    def vazia(self):
        return len(self._nos) == 0

    @abstractmethod
    def inserir(self, no):
        raise NotImplementedError("Inserir No Fronteira")
    """
    Metodo que removo o primeiro no da fronteira
    """
    def remover(self):
        return self._nos.pop(0)
