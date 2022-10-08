from .comportamento import Comportamento

"""
ACOPLAMENTO
baixo, nao depende muito de outras classes para funcionar

COESÃO
é muito coeso, realiza penas uma funçao - ativar

SIMPLICIDADE
 - simples de explicar,  cada função e sucinta e facil de entender

Mecanismo de reacao que consiste na regra estímulo - resposta

recebe uma percepcao e devolver uma accao,
segue o modelo reactivo
"""

"""
Classe que corresponde a reacao (mecanismo de reacao)
"""
class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        self._estimulo = estimulo
        self._resposta = resposta

    """
    Método que ativa o mecanismo de reacao retornando uma accao
    """

    def activar(self, percepcao):
        instensidade = self._estimulo.detectar(percepcao)  # deteta a percepcao
        if instensidade > 0:  # verifica se a intensidade do estimulo > 0
            # a accao e ativada baseada na percepcao e na intensidade
            return self._resposta.activar(percepcao, instensidade)
