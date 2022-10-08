from abc import abstractmethod


"""
Classe que representa o Estado
Este estado é uma representação da configuracao de um sistema ou problema, sendo uma identificacao unica
Contem um espaco de estado onde e um conjunto e transicoes de estado
"""
class Estado:

    @abstractmethod
    def id_valor(self):
        raise NotImplementedError("Valor ID")


    def __hash__(self):
        return self.id_valor() 

    def __eq__(self,other):
        return self.__hash__() == other.__hash__()
