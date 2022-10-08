from abc import ABC, abstractmethod

"""
Classe que representa o operador
Este operador representa uma acao, que gera essa transformacao de estado
"""


class Operador(ABC):

    @abstractmethod
    def aplicar(self, estado):
        raise NotImplementedError("Aplicar Operador ao estado")

    @abstractmethod
    def custo(self, estado, estado_suc):
        raise NotImplementedError("Custo do operador")
