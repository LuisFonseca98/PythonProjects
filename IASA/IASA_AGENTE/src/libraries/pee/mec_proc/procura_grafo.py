
"""
Classe que representa a procura em grafos
Neste tipo de procura existem estados repetidos na arvore de procura
->Grafo de espacos de estados apresenta ciclos
->Multiplas transicoes para o mesmo estado
->Accoes correspondentes as transicoes de estado reversiveis
A expansao de estados ja anteriormente analisados apresenta desperdicio de 
recursos (em termos computacionais, tempo e memoria)

Os tipos de nos que explora sao:
->abertos: que sao nos gerados mas nao expandidos (aqueles na fronteira de exploracao)
->fechados: que sao nos expandidos

"""
from abc import ABC

from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura,ABC):

    """
    Mecanismo geral de procura em grafos
    """
    def resolver(self,problema):
        self._explorados = {}
        return super().resolver(problema)

    """
    Metodo que memoriza os nos explorados, e insere na fronteira
    """
    def _memorizar(self,no):
        estado = no.estado
        if self._manter(no):
            self._explorados[estado] = no
            self._fronteira.inserir(no)

    """
    Metodo que mantem o estados dos nos explorados
    """
    def _manter(self,no):
        return no.estado not in self._explorados


