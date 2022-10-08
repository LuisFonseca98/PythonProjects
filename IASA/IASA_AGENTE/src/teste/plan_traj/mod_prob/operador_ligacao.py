from mod.operador import Operador

"""
Classe que representa o operador de ligacao
"""
class OperadorLigacao(Operador):

    """
    Construtor da classe que necesstia de conhecer o custo, estado origem e destino
    """
    def __init__(self, origem, destino, custo):
        self._custo = custo
        self._estado_origem = origem
        self._estado_destino = destino

    """
    Classe que aplica o estado, verificando se o estado e o de origem
    Caso seja, retorna o estado destino
    """
    def aplicar(self, estado):

        #if estado.__eq__(self._estado_origem):
            #return self._estado_destino

        if self._estado_origem == estado:
            return self._estado_destino

    """
    Metodo que retorna o custo
    """
    def custo(self, estado, estado_suc):
        return self._custo