from abc import ABC, abstractmethod

"""
Sendo esta classe uma interface, funciona como um contrato para interacao com o exterior

introduz o conceito de abstracao para lidar com a complexidade. separa o que e relevante e o que não é
"""


class Estimulo(ABC):

    @abstractmethod
    def detectar(self, percepcao):
        raise NotImplementedError("Activa estimulo")

