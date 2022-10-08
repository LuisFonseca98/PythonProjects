

from mod.passo_solucao import PassoSolucao

"""
Classe que representa a solucao do problema
"""
class Solucao:

    """
    Construtor que inicializa a solucao
    Inicia um percurso, e insere um no, sempre que encontra uma posicao livre
    """
    def __init__(self, no_final):
        self._percurso = []
        no = no_final
        while no:
            self._percurso.insert(0, no)
            no = no.antecessor

    """
    Metodo que remove um passo de solucao, na fronteira de exploracao
    """
    def remover_passo(self):
        if self.dimensao > 1:
            estado = self._percurso[0].estado
            operador = self._percurso[1].operador
            self._percurso.pop(0)
            return PassoSolucao(estado,operador)

    """
    Metodo que retorna o iterador da lista (neste caso do percurso)
    """
    def __iter__(self):
        return iter(self._percurso)

    """
    Metodo que retorno o "index" da lista do percurso
    """
    def __getitem__(self, index):
        return self._percurso[index]

    @property
    def dimensao(self):
        return len(self._percurso)

    @property
    def custo(self):
        return self._percurso[self.dimensao - 1].custo
