

from abc import ABC, abstractmethod


class SelAccao(ABC):

    @abstractmethod
    def seleccionar_accao(self,s):
        raise NotImplementedError("selecionar accao aprend ref")

