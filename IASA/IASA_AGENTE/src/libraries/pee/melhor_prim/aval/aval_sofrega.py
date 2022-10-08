




"""
Mecanismo de procura sofrega
Criterio de ordem: f(n) = h(n)
"""


from pee.melhor_prim.aval.aval_heur import AvalHeur


class AvalSofrega(AvalHeur):

    def prioridade(self,no):
        return self._heuristica.h(no.estado)