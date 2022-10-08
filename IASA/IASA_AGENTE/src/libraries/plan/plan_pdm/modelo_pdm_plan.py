



from pdm.modelo_pdm import ModeloPDM


class ModeloPDMPlan(ModeloPDM):


    def __init__(self,modelo_plan,objectivos):
        self._rmax = 1000
        self._objectivos = objectivos
        self._modelo_plan = modelo_plan

    def estado(self):
        return self._modelo_plan.estado()

    def estados(self):
        return self._modelo_plan.estados()

    def operadores(self):
        return self._modelo_plan.operadores()

    def S(self):
        return self.estados()

    def A(self, s):
        if s in self._objectivos:
            return []
        return self.operadores()

    def T(self, s, a):
        sn = a.aplicar(s)
        if sn:
            return [(1,sn)] #Determinista logo so tem uma opcao
        return []
        
    def R(self, s, a, sn):
        if sn in self._objectivos:
            return self._rmax - a.custo(s,sn)
        return -a.custo(s,sn)