from abc import ABC
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


"""
Classe que correposnde a procura informada
"""
class ProcuraInformada(ProcuraMelhorPrim, ABC):

    """
    Metodo resolver que resolve um problema, conhecendo a heuristica
    """
    def resolver(self, problema,heuristica):
        self._heuristica = heuristica
        return super().resolver(problema)