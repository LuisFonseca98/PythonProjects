


from abc import ABC, abstractmethod


class MemoriaAprend(ABC):

    @abstractmethod
    def q(self,s,a):
        raise NotImplementedError("metodo q aprend ref")

    @abstractmethod
    def actualizar(self,s,a,q):
        raise NotImplementedError("actualizar aprend ref")

    @abstractmethod
    def obter_estados(self):
        raise NotImplementedError("obter estados aprend ref")

