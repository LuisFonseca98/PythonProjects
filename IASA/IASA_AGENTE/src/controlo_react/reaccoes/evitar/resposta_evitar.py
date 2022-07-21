from random import choice

from sae import Direccao

from ..resposta.resposta_mover import RespostaMover

"""
Classe que representa a resposta do evitar
"""
class RespostaEvitar(RespostaMover):

    """
    Construtor que permite inicializar consoante uma direcao inicial
    Neste caso, quando encontra o obstaculo, o agente evita-o, movendo para a direcao ESTE
    """
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self._direccoes = list(Direccao)


    
    """
    Método que permite ativar a resposta evitar, quando o agente encontra o obstaculo
    """
    def activar(self, percepcao, intensidade):
        contacto_obst = percepcao.contacto_obst(self._accao.direccao)
        if contacto_obst:
            direccao_livre = self._direccao_livre(percepcao)
            if direccao_livre:
                self._accao.direccao = direccao_livre
                contacto_obst = False

        if not contacto_obst:
            return super().activar(percepcao, intensidade)

    """
    Metodo que verifica a direcao livre, onde o agente se pode movimentar, nao encontrando um obstaculo
    """
    def _direccao_livre(self, percepcao):
        dir_livres = [
            direccao for direccao in Direccao if not percepcao.contacto_obst(direccao)]
        return choice(dir_livres)
