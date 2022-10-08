from abc import abstractmethod

from .comportamento import Comportamento

'''
Classe que representa um comportamento composto. Neste caso seria o agente efetuar um conjunto de comportamentos
Evitar obstaculos
Apanhar alvos
Explorar o ambiente

'''

class ComportComp(Comportamento):
    '''
    Construtor que inicializa os diferentes comportamentos que irão ser passados
    '''
    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    '''
    Metodo que ativa as diferentes accoes
    Caso nao retorne nenhuma accao, coloca na lista de accoes
    Caso a lista nao contenha nenhuma accao, retorna a accao selecionada
    '''
    def activar(self, percepcao):
        accoes = []
        for comportamento in self._comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            return self.selecionar_accao(accoes)

    '''
    Classe que seleciona uma accao, da lista de accoes
    '''
    @abstractmethod
    def selecionar_accao(self, accoes):
        raise NotImplementedError("Seleciona accao")

