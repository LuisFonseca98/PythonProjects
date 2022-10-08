
"""
Classe que corresponde ao controlo deliberativo do agente
"""
from pee.control_delib.modelo_mundo import ModeloMundo
from sae.agente.controlo import Controlo
from sae.ambiente.elemento import Elemento


class ControloDelib(Controlo):

    """
    Construtor que inicializa o modelo mundo, objectivos e planeador
    """
    def __init__(self,planeador):
        self._planeador = planeador
        self._modelo_mundo = ModeloMundo()
        self._objectivos = [] #sendo deliberativo e necessario criar

    """
    Metodo que "processa" uma ação segundo a estratégia:
    1-observa o mundo em sem redor
    2-Atualiza as crenças
    3-Se reconsiderar, pode deliberar ou planear
    4-Executa planos de ação
    """
    def processar(self, percepcao):
        self._assimilar(percepcao) #assimilia a percepcao
        print("Posicoes do agente", self._modelo_mundo.estado()._posicao)
        if self._reconsiderar(): #verifica se reconsidera. Caso sim, vai deliberar e planear
            self._deliberar() 
            self._planear()
        self._mostrar()
        return self._executar() #executa a accao, com ou sem deliberar e planear

    """
    Metodo que atualiza o modelo do mundo, consoante uma percepcao
    """
    def _assimilar(self,per):
        self._modelo_mundo.actualizar(per)

    """
    Metodo que indica se é necessário voltar a deliberar ou planear
    """
    def _reconsiderar(self):
        if self._modelo_mundo._alterado or not self._planeador.plano_valido(self._modelo_mundo.estado()):
           return True
        else:
            return False
        

    """Raciocionia acerca dos fins - gera os objetivos"""
    def _deliberar(self):
        self._objectivos = [estado for estado in self._modelo_mundo.estados() 
                           if self._modelo_mundo.obter_elem(estado) == Elemento.ALVO]
        
        
    """
    Metodo que verifica se existe objectivos
    Caso exista, vai planear, caso contrario termina o plano
    """
    def _planear(self):
        if self._objectivos:
            self._planeador.planear(self._modelo_mundo,
            self._objectivos)
        else:
            self._planeador.terminar_plano()

    """executa o operador(muda de estado)"""
    def _executar(self):
        operador = self._planeador.obter_accao(self._modelo_mundo.estado())

        if operador: return operador.accao

    def _mostrar(self):
        self.vista.limpar()
        self._modelo_mundo.mostrar(self.vista)
        self._planeador.mostrar(self.vista)
        self.vista.mostrar_estados(self._objectivos)


