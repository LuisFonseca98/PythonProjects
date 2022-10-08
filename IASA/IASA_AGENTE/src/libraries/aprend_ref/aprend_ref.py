

from abc import ABC, abstractmethod

"""
Classe que representa a aprendizagem por reforco
"""
class AprendRef(ABC):

    def __init__(self,mem_aprend,sel_accao):
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    @abstractmethod
    def aprender(self,s,a,r,sn):
        raise NotImplementedError("Aprender Apred Ref")