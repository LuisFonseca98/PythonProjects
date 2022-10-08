
"""
Mecanismo de procura heuristica
"""


from pee.mec_proc.fronteira.avaliador import Avaliador


class AvalHeur(Avaliador):

    def __init__(self ,heuristica):
        self._heuristica = heuristica
