"""
Classe que representa a procura limitada

A Diferença da procura de profundidade Limitada é que esta procura em 
profundidade limite que verifica na expansão de nós, quando a profundidade 
limite for atingida. Caso seja alcancada não é realizada mais expansão de nós 
e a fronteira fica vazia o que faz com que termine a sua resolução

"""


from pee.prof.procura_prof import ProcuraProf


class ProcuraProfLim(ProcuraProf):
    """
    Metodo resolver
    """
    
    def resolver(self, problema, prof_max=100):
        self._prof_max = prof_max
        return super().resolver(problema)

    "Metodo expandir, que expande a procura em profundidade"

    def _expandir(self, problema, no):
        if no.profundidade > self._prof_max:
            return
        elif not self.ciclo(no):
            yield from super()._expandir(problema, no)

    "Representa um ciclo na arvore de nos, da procura em profundidade"

    def ciclo(self, no):
        no_ant = no.antecessor
        while no_ant:
            if no.estado == no_ant.estado:
                return True
            no_ant = no_ant.antecessor
        return False
