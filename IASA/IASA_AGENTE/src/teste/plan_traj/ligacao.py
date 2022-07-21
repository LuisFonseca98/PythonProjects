from dataclasses import dataclass

"""
Classe que representa um conjunto de atributos
"""
@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int