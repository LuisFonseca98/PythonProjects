from .comportamento_comp import ComportComp

"""Como esta definido ns slides,
 a prioridade elege uma accao baseada num conjunto de fatores. neste caso, por exemplo, 
 seria a direccao para onde se mover (Explorar): Norte Sul Este oeste """


class Prioridade(ComportComp):
    def selecionar_accao(self, accoes):
        return max(accoes, key=lambda accao: accao.prioridade)
