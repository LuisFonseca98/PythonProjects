
from mod.solucao import Solucao
from pee.larg.procura_larg import ProcuraLarg
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.prof.procura_prof import ProcuraProf
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from teste.plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj

"""
Classe que representa o planeador de  trajetos
"""
class PlaneadorTrajeto:

    """
    Metodo que vai planear o trajeto, consoante as diferentes procuras que irao ser testadas
    """
    def planear(self, ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        listaProcuras = [

            #ProcuraProf(),
            #ProcuraProfLim(),
            #ProcuraProfIter(),
            #ProcuraLarg(),
            ProcuraCustoUnif(),

        ]

        return listaProcuras[0].resolver(problema)

    """
    Metodo que mostra o trajeto, imprimindo na consola a solucao
    """
    def mostrar_trajecto(self, solucao):
        #for no in iter(solucao):
        #for no in solucao._percurso:
        for no in Solucao.__iter__(solucao):
            if isinstance(no.estado,str):
                print(no.estado)
            else:
                print(no.estado.localidade)