from abc import abstractmethod, ABC
from pee.mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade

from pee.mec_proc.procura_grafo import ProcuraGrafo


"""
Classe que representa a procura melhor-primeiro
Este tipo de procura tira partido de uma availiacao de estado
Utiliza uma funcao "f" para avaliacao de cada no "n" gerado
-> "f(n) > 0"
-> "f(n)" representa uma estimativa do custo da solucao atraves do no "n"
  --> quando menor o valor de "f(n)" mais promissor e o no "n"
A fronteira de exploracao e ordenada por ordem crescente f(n)
"""


class ProcuraMelhorPrim(ProcuraGrafo, ABC):

    def _iniciar_fronteira(self):
        return FronteiraPrioridade(self.iniciar_avaliador())

    def _manter(self, no):
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo

    @abstractmethod
    def iniciar_avaliador(self):
        raise NotImplementedError("Valor ID")
