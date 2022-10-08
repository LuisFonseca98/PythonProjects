"""
Agente de simulação
@author: Luís Morgado
"""

from .transdutor import Transdutor

#_______________________________________________________________________________

class Agente:
    """
    Agente base para simulação
    """
    def __init__(self, ambiente, controlo):
        self.__controlo = controlo
        self.__transdutor = Transdutor(ambiente)

    @property
    def controlo(self):
        return self.__controlo
    
    def executar(self):
        """
        Executar passo de processamento
        """
        percepcao = self.__transdutor.percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__transdutor.actuar(accao)
