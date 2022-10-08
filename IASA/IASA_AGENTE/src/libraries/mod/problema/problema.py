from abc import ABC, abstractmethod

"""
Classe que define o problema (associando ao raciocinio automatico)
O problema ira conter um estado inicial, operadores e objectivos
Podemos associar o estado ao objectivo que retorna true ou false
"""


class Problema(ABC):

    """
    Construtor do problema, onde necessita sempre de conhecer o estado inicial
    e um conjunto de operadores
    """
    def __init__(self, estado_inicial, operadores):
        self._estado_inicial = estado_inicial
        self._operadores = operadores
        
    @abstractmethod
    def objectivo(self, estado):
        raise NotImplementedError("Objetivo problema")

    @property
    def operadores(self):
        return self._operadores
    
    @property
    def estado_inicial(self):
        return self._estado_inicial
