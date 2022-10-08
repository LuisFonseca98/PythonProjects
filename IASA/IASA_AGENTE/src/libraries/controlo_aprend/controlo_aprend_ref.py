
from controlo_aprend.mec_aprend import MecAprend
from mod.agente.estado_agente import EstadoAgente
from sae import Controlo
from sae.agente.accao import Accao
from sae.ambiente.direccao import Direccao

"""
Classe que representa o controlo de aprendizagem
"""
class ControloAprendRef(Controlo):


    """
    Construtor que conhece um valor r (min e max)
    estado e accoes (consoante uma direcao)
    """
    def __init__(self):
        self._rmax = 100.0 #valor maximo do reforco
        self._rmin = 1 #valor minimo do reforco
        self._s = None
        self._a = None
        accoes = [Accao(direcao) for direcao in Direccao]
        self._mec_aprend = MecAprend(accoes)

    """
    Metodo que processa o controlo da aprendizagem por reforco
    consoante as posicoes do agente
    """
    def processar(self, percepcao):
        sn = EstadoAgente(percepcao.posicao) #estado seguinte do agente
        an = self._mec_aprend.selecionar_accao(sn)
        r = self._gerar_reforco(percepcao)
        if self._s is not None and self._a is not None:
            self._mec_aprend.aprender(self._s,self._a,r,sn)
        self._s = sn
        self._a = an
        self._mostrar()
        return an

    """
    Metodo que gera reforco ao agente
    Caso encontre um obstaculo, e adicionado um reforco negativo
    caso faca a recolha, e adicionado um reforco positivo
    """
    def _gerar_reforco(self,percepcao):
        reforco = -1 * self._rmin #sempre que da um passo, ja recebe um reforco negativo (ou castigo)
        if percepcao.recolha: 
            reforco += self._rmax
        elif percepcao.colisao:
            reforco += -1 * self._rmax
        return reforco

    def _mostrar(self):
        estados = self._mec_aprend.estados
        politica = {s: self._mec_aprend.accao_sofrega(s) for s in estados}
        valor = {s: self._mec_aprend.q(s, politica[s]) for s in estados}
        self.vista.limpar()
        self.vista.mostrar_valor(valor)
        self.vista.mostrar_politica(politica)