
"""
Mecanismo de procura custo uniforme
Criterio de ordem: f(n) = g(n) 
"""


from pee.mec_proc.fronteira.avaliador import Avaliador


class AvalCustoUnif(Avaliador):

    def prioridade(self, no):
        return no.custo
