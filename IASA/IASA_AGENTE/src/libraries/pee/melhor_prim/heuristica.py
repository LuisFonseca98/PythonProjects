from abc import ABC, abstractmethod

"""
Classe que corresponde a funcao heuristica


Esta funcao representa uma estimativa do custo do percurso
desde o no ate ao no objectivo

Reflete conhecimento acerca do dominio do problema para guiarr a procura

O seu valor e independente do percurso ate "n"

Depende apenas do estado associado a n e do objectivo

"""


class Heuristica(ABC):

    @abstractmethod
    def h(self, estado):
        raise NotImplementedError("Procura Heuristica")
