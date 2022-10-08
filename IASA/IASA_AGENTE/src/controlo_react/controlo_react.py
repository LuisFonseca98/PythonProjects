from sae import Controlo


"""
Classe que corresponde ao controlo reactivo
"""
class ControloReact(Controlo):

    """
    Construtor que inicializa os diferentes atributos
    Necesita de conhecer a direcao, e o respetivo comportamento
    """
    def __init__(self, comportamento):
        self.mostrar_per_dir = True
        self._comportamento = comportamento

    """Metodo que activa o comportamento, consoante a percepcao passada, i.e Reage"""
    def processar(self, percepcao):
        return self._comportamento.activar(percepcao)
