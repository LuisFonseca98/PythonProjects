from abc import ABC, abstractmethod

"""
Sendo esta classe uma interface, funciona como um contrato para interacao com o exterior

Introduz o conceito de abstracao para lidar com a complexidade. separa o que e relevante e o que não é
"""


class Comportamento(ABC):

    @abstractmethod
    def activar(self, percepcao):
        raise NotImplementedError("Activa Comportamento")

