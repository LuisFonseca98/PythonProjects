

from mod.problema.problema import Problema
from teste.plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from teste.plan_traj.mod_prob.operador_ligacao import OperadorLigacao

"""
Classe que representa o problema para resolver o planeador de trajeto
"""
class ProblemaPlanTraj(Problema):

    """
    Construtor que necessita de conhecer o estado final
    Necessita de uma lista de operadores, visto que iremos obter um operador de ligacao
    onde necessita de conhecer a origem, destino e o custo dessa ligacao
    """
    def __init__(self, ligacoes, loc_inicial, loc_final):
        self._estado_final = EstadoLocalidade(loc_final)
        operadores = []
        for lig in ligacoes:
            operador = OperadorLigacao(lig.origem, lig.destino, lig.custo)
            operadores.insert(0, operador)
        super().__init__(EstadoLocalidade(loc_inicial), operadores)

    """
    Metodo que verifica se o problema chegou ao destino (ou se resolveu o problema
    ou se chegou ao estado final)
    """
    def objectivo(self, estado):
        #if estado.__eq__(self._estado_final):
            #return True
        #return False
        
        return self._estado_final == estado
