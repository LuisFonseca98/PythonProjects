
"""
Classe que corresponde  a procura sofrega

Esta procura corresponde a uma das tres variantes principais da
procura melhor primeiro

f(n) = h(n), ou seja nao tem em conta o custo do percurso explorado.
Minimiza o custo local e tem solucoes sub-otimas(problema de otimos locais)

"""
from abc import ABC
from pee.melhor_prim.aval.aval_sofrega import AvalSofrega
from pee.melhor_prim.procura_informada import ProcuraInformada



class ProcuraSofrega(ProcuraInformada, ABC):

    def iniciar_avaliador(self):
        return AvalSofrega(self._heuristica)
