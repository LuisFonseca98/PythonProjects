from abc import ABC, abstractmethod

from mod.mec_proc.no import No
from mod.problema.problema import Problema
from mod.solucao import Solucao


"""
Classe que representa o mecanismo de procura
"""


class MecanismoProcura(ABC):

    def __init__(self):
        #self._fronteira = self._iniciar_fronteira() ## Inicia a fronteira de exploração
        self._fronteira = None
        #self._nos_processados = 0
        #self._nos_memorizados = 0
    """
    Metodo resolver do mecanismo de procura
    Este metodo ira ser usado por todas as procuras, resolvendo o seu problema
    """
    def resolver(self, problema):

        self._fronteira = self._iniciar_fronteira() #iniciasse a fronteira
        no = No(problema.estado_inicial) #e criado um no que contem um estado inicial para o problema
        if problema.objectivo(no.estado):## Verificaca se o estado inicial(a partir do problema) é a solucao
            #print("Numero de nos processados:", self._nos_processados)
            #print("Numero de nos processados:", self._nos_memorizados)
            return Solucao(no) ## Caso seja o estado inicial retorna a Solução
        self._memorizar(no) ## Memoriza o nó no dicionário dos já explorados e na fronteira, ou só na fronteira
        while not self._fronteira.vazia():## Enquanto existirem caminhos para expandir e explorar na fronteira o Algoritmo é executado
            no = self._fronteira.remover() #remove da fronteira o no
            for no_suc in self._expandir(problema, no): #percorre a lista de nos, a medida que expande
                estado = no_suc.estado #atualizado o estado, atraves do estado sucessor
                if problema.objectivo(estado):
                    return Solucao(no_suc) #caso o objectivo corresponda ao estado, retorna a soluca
                self._memorizar(no_suc) #memoriza o estudo sucessor
        return None #retorna None caso nao encontre nenhuma solucao
     

    @abstractmethod
    def _iniciar_fronteira(self):
        raise NotImplementedError("Inicia a fronteira")

    '''
    Metodo que permite expandir a procura em nos
    '''

    def _expandir(self, problema:Problema, no:No):
        for operador in problema.operadores:  # iteracao de cada operador
            estado_suc = operador.aplicar(no.estado)  # aplica o estador seguinte, no estado atual
            if estado_suc:# condicao de verificacao do estado sucessor. Se true, expande para outro no
                yield No(estado_suc, operador, no)  # cria um novo no, atraves do estado sucessor, com o operador

    
        # o yield permite:
        # for no_suc in self.expandir(...):

    @abstractmethod
    def _memorizar(self, no):
        raise NotImplementedError("Memoriza a fronteira")
