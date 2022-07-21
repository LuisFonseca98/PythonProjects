from ecr.hierarquia import Hierarquia
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obst import EvitarObst
from .explorar.explorar import Explorar


"""
Classe que representa o comportamento Recolher
Nesta classe contemos uma hierarquia fixa, com diversos comportamentos
Podemos dizer que este comportamento é um comportamento composto, visto que pode acionar outros comportamentos
"""
class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()])
