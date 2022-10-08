

from abc import ABC, abstractmethod


class ModeloPlan(ABC):

    @abstractmethod
    def estado(self):
        raise NotImplementedError("estado")

    @abstractmethod
    def estados(self):
        raise NotImplementedError("estados")

    @abstractmethod
    def operadores(self):
        raise NotImplementedError("operadores")