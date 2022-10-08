from .comportamento_comp import ComportComp

"""Como definido nos slides, o agente vai sempre selecionar a accao com maior nivel hierarquico: Apanhar alvo, evitar obstaculo e explorar. respectivamente"""


class Hierarquia(ComportComp):
    def selecionar_accao(self, accoes):
        return accoes[0]
