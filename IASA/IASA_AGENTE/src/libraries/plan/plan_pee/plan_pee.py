

"""
Classe que corresponde ao planeador em PEE(procura em espaco de estados)

Esta classe corresponde a um dos metodos de planeamento automatico
onde recebe um objectivo e um modelo de planeamento

O raciocinio automatico e orientado para a geracao de estrategias 
ou planos de acao em particular para a execucao de agentes inteligentes

"""
from pee.melhor_prim.procura_AA import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofregra import ProcuraSofrega
from plan.plan_pee.heur_dist import HeurDist
from plan.plan_pee.problema_plan import ProblemaPlan
from plan.planeador import Planeador



class PlanPEE(Planeador):
 
    """
    Construtor da classe que conhece uma solucao e um tipo de procura.
    Para testes, ira ser testado a ProcuraCustoUnif
    """
    def __init__(self):
        self._solucao = None
        self._mec_pee = ProcuraAA()
        #self._mec_pee = ProcuraSofrega()
        #self._mec_pee = ProcuraCustoUnif()

    """
    Metodo que resolve um problema passando uma heuristica
    """
    def planear(self, modelo_plan, objectivos):
        estado_final = objectivos[0]
        #problema = ProblemaPlan(modelo_plan,estado_final)
        #self._solucao = self._mec_pee.resolver(problema)
        problema = ProblemaPlan(modelo_plan,estado_final)
        heuristica = HeurDist(estado_final)
        self._solucao = self._mec_pee.resolver(problema,heuristica)
    """
    Metodo que obtem uma acao, removendo um passo

    """
    def obter_accao(self, estado):
        if self._solucao:
            removerPasso = self._solucao.remover_passo()
            if (estado.__eq__(removerPasso.estado)):
                return removerPasso.operador
        

    
    """
    Metodo que verifica se existir solucao e o primeiro passo da solução corresponder ao estado atual do agente
    """
    
    def plano_valido(self, estado):
        if self._solucao != None and estado.__eq__(self._solucao.__getitem__(0).estado):
            return True
        else:
            return False

    def terminar_plano(self):
        self._solucao = None

    def mostrar(self,vista):
        vista.mostrar_solucao(self._solucao)