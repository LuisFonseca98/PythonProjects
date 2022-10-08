"""
Classe que representa a fronteiraFIFO
(First In First Out)
"""


from mod.fronteira import Fronteira


class FronteiraFIFO(Fronteira):

    def inserir(self, no):
        self._nos.append(no)
