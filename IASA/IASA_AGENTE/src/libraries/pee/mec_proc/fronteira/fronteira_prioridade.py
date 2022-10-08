from heapq import heappush, heappop

from mod.fronteira import Fronteira


"""
Classe que representa a fronteira de prioridade
"""
class FronteiraPrioridade(Fronteira):

    """
    Construtor que herda os metodos e atributos da fronteira
    """
    def __init__(self, avaliador):
        self._avaliador = avaliador
        super().__init__()
    
    """
    Metodo que insere os nos, com maior prioridade
    """
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    """
    Metodo que remove os nos mais antigos na fronteira 
    """
    def remover(self):
        (_, no) = heappop(self._nos)
        return no
