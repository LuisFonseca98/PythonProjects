
"""
Classe que representa o nó, servindo de uma etapa de procura
Corresponde a árvore de procura, onde contém uma raiz: corresponde ao no inicial
Contem uma fronteira de exploracao que consiste no criterio de ordenacao
"""

class No:

    """
    Construtor que inicializa os diferentes atributos
    O no necessita de conhecer o respetivo estado,
    o operador para efetuar a mudanca de estado
    o antecessor para conhecer o respectivo no
    """
    def __init__(self, estado, operador=None, antecessor=None):
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor

        if antecessor is None:
            self._profundidade = 0
            self._custo = 0
        else:
            self._profundidade = antecessor.profundidade + 1
            self._custo = antecessor.custo + operador.custo(estado, antecessor.estado)
        
        

    """
    Método que compara o custo do no, com o no antecessor
    """
    def __lt__(self, no):
        return self.custo < no.custo

    @property
    def profundidade(self):
        return self._profundidade
    
    @property
    def custo(self):
        return self._custo
    
    @property
    def antecessor(self):
        return self._antecessor
    
    @property
    def operador(self):
        return self._operador
    
    @property
    def estado(self):
        return self._estado
