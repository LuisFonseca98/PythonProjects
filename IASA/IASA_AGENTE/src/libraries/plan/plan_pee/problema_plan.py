



"""
Classe que corresponde ao planeador do problema
"""
from mod.problema.problema import Problema
from plan.modelo_plan import ModeloPlan


class ProblemaPlan(Problema):


    """
    Construtor que recebe um estado e o modelo do plan
    """

    def __init__(self, modelo_plan:ModeloPlan, estado_final):
        super().__init__(modelo_plan.estado(),modelo_plan.operadores())
        self._estado_final = estado_final

    """
    Metodo que obtem o objectivo.
    Verificando quando o estado atinge o estado final
    """
    def objectivo(self, estado):
        #return estado == self._estado_final
        if estado.__eq__(self._estado_final):
            return True
        else:
            return False
        