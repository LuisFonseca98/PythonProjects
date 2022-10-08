"""
Classe que representa a procura em profundidade iterativa

A Procura em profundidade iterada funciona como a procura profundidade limite apenas com a 
diferença que a profundidade limite vai ser aumentada incrementalmente, ou seja, se os 
incrementos forem de dois a procura vai sair do nó inicial para o primeiro nó da árvore de nós
de seguida expande esse nó e verifica o primeiro que entrou na fronteira destes dois nós 
expandidos, depois verifica o segundo, se nenhum deles for a solucao volta a para a profundidade 
e continua a execução

"""


from pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """
    Metodo resolver, retornando uma solucao, consoante a profundidade passada (inicial e final)
    """

    def resolver(self, problema, inc_prof=1, prof_max=1000):
        for profundidadeAtingir in range(inc_prof, prof_max, inc_prof):
            solucao = ProcuraProfLim.resolver(self, problema, profundidadeAtingir)
            if solucao is not None:
                return solucao
