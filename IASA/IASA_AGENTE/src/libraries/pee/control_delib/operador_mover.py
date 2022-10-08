

"""
Classe do operador mover
"""
import math
from mod.agente.estado_agente import EstadoAgente
from sae.agente.accao import Accao


class OperadorMover:

    """
    Construtor que inicializa os diferentes atributos
    Necessita de conhecer um angulo um modelo do mundo e uma accao
    Essa accao necessita de conhcer o angulo
    """
    def __init__(self,modelo_mundo,direcao):
        self._ang = direcao.value
        self._modelo_mundo = modelo_mundo
        self._accao = Accao(direcao)
    
    """
    Metodo que aplica um novo estado
    """
    def aplicar(self,estado): 
        posX,posY = estado.posicao
        passoAccao = self._accao.passo
        distX = round(passoAccao * math.cos(self._ang))
        distY = -round(passoAccao * math.sin(self._ang))
        novaPosX = posX + distX
        novaPosY = posY + distY
        novaPos = novaPosX, novaPosY
        novo_estado = EstadoAgente(novaPos)
        if novo_estado in self._modelo_mundo.estados():
            return novo_estado
         
    """
    Representa o custo,  fazendo a distancia entre o estado atual e o novo estado
    """
    def custo(self,estado,novo_estado):
        return max(1,math.dist(estado.posicao,novo_estado.posicao))

    @property
    def ang(self):
        return self._ang

    @property
    def accao(self):
        return self._accao