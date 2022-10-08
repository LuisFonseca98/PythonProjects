


from abc import ABC, abstractmethod


class Planeador(ABC):

    @abstractmethod
    def planear(self,modelo_plan,objectivos):
        raise NotImplementedError("Metodo planear")

    @abstractmethod
    def obter_accao(self,estado):
        raise NotImplementedError("Obter Accao")

    @abstractmethod
    def plano_valido(self,estado):
        raise NotImplementedError("Plano valido")

    @abstractmethod
    def terminar_plano(self):
        raise NotImplementedError("Terminar Plano")
    