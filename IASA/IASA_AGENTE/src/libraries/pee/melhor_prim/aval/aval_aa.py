




"""
Mecanismo de procura A*
Criterio de ordem: f(n) = g(n) + h(n)
"""


from pee.melhor_prim.aval.aval_heur import AvalHeur


class AvalAA(AvalHeur):

    def prioridade(self,no):
        return no.custo + self._heuristica.h(no.estado)