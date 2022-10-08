"""
Classe que representa a fronteiraLIFO
(Last In First Out)
"""


from mod.fronteira import Fronteira


class FronteiraLIFO(Fronteira):

    def inserir(self, no):
        self._nos.insert(0, no)
