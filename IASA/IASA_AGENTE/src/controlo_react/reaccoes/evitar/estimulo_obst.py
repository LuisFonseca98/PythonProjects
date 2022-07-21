from ecr.estimulo import Estimulo


"""
Classe que representa o estimulo obstaculo
"""
class EstimuloObst(Estimulo):

    """
    Construtor que necessita de conhecer a direcao e a intensidade
    """
    def __init__(self, direccao, intensidade=1):
        self._direccao = direccao
        self._intensidade = intensidade

    """
    Método que permite detetar o obstaculo, quando entra em contato com este
    """
    def detectar(self, percepcao):
        if percepcao.contacto_obst(self._direccao):
            return self._intensidade
        else:
            return 0
