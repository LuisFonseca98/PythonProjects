from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador

"""
Classe que engloba um estado e um operador
"""
@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador
