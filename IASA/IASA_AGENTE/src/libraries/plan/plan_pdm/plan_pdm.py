


from pdm.pdm import PDM
from plan.plan_pdm.modelo_pdm_plan import ModeloPDMPlan
from plan.planeador import Planeador


class PlanPDM(Planeador):

    def __init__(self):
        self._gama = 0.9
        self._delta_max = 1
        self._utilidade = None
        self._politica = None

    def planear(self, modelo_plan,objectivos):
        modeloPDM = ModeloPDMPlan(modelo_plan,objectivos)
        pdm = PDM(modeloPDM,self._gama,self._delta_max)
        self._utilidade,self._politica = pdm.resolver()

    def obter_accao(self, estado):
        if self.plano_valido(estado):
            return self._politica[estado]

    
    def plano_valido(self, estado):
        if self._politica != None and self._politica[estado] != None:
            return True
        else:
            return False

    def terminar_plano(self):
        self._politica = None
        self._utilidade = None
    
    def mostrar(self,vista):
        vista.mostrar_valor(self._utilidade)
        if self._politica:
            vista.mostrar_politica(self._politica)