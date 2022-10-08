

from abc import ABC,abstractmethod


class ModeloPDM(ABC):

    """
    Metodo S -> conjunto de estados do mundo
    """
    @abstractmethod
    def S(self):
        raise NotImplementedError("Estado")

    """
    Metodo A(s) ->  conjunto de acções possíveis no estado s pertence a S
    """
    #s -> estado
    @abstractmethod
    def A(self,s):
        raise NotImplementedError("Accao")

    """
    Metodo T(s,a,s') -> probabilidade de transição de s para s' através de a
    """
    #s -> estado
    #a -> operador
    @abstractmethod
    def T(self,s,a):
        raise NotImplementedError("Transicao")

    """
    Metodo R(s,a,s') -> recompensa esperada na transição de s para s' através de a
    """
    #s -> estado
    #a -> operador
    #sn -> estado seguinte
    @abstractmethod
    def R(self,s,a,sn):
        raise NotImplementedError("Recompensa")