
from teste.plan_traj.ligacao import Ligacao
from teste.plan_traj.planeador_trajecto import PlaneadorTrajeto


"""
Classe de testes, testando o correto comportamento da solucao
"""


ListaLigacoes = [
Ligacao("Loc-0","Loc-1",5),
Ligacao("Loc-0","Loc-2",25),
Ligacao("Loc-1","Loc-3",12),
Ligacao("Loc-1","Loc-6",5),
Ligacao("Loc-2","Loc-4",30),
Ligacao("Loc-3","Loc-2",10),
Ligacao("Loc-3","Loc-5",5),
Ligacao("Loc-4","Loc-3",2),
Ligacao("Loc-5","Loc-6",8),
Ligacao("Loc-5","Loc-4",10),
Ligacao("Loc-6","Loc-3",15),
]

print("Solução: ")
solucao = PlaneadorTrajeto().planear(ListaLigacoes, "Loc-0", "Loc-4")
PlaneadorTrajeto().mostrar_trajecto(solucao)