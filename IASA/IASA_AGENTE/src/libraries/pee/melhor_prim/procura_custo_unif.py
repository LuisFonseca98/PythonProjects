"""
Classe que corresponde  a procura de custo uniforme

Esta procura corresponde a uma das tres variantes principais da
procura melhor primeiro

f(n) = g(n), ou seja nao tira partido de conhecimento do dominio 
do problema expresso atraves da funcao h(n)

"""


from pee.melhor_prim.aval.aval_custo_unif import AvalCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraCustoUnif(ProcuraMelhorPrim):

    def iniciar_avaliador(self):
        return AvalCustoUnif()
