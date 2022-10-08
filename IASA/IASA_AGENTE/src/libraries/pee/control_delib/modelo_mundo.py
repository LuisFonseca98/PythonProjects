


"""
Classe que corresponde ao modelo do mundo
"""
from mod.agente.estado_agente import EstadoAgente
from pee.control_delib.operador_mover import OperadorMover
from plan.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao


class ModeloMundo(ModeloPlan):

    """
    Construtor que inicializa os diferentes atributos
    Operador vai precisar de  consoaonte um angulo para uma determinada direcao
    """
    def __init__(self):
        self._estado = None
        self._estados = []
        self._alterado = True
        self._elementos = dict()
        self._operadores = [OperadorMover(self,angle) for angle in Direccao]
    
    """
    Atualiza o estado consoante a posicao
    """

    def actualizar(self, percepcao):
        self._estado = EstadoAgente(percepcao.posicao) #o estado sera a posicao do agente, consoante a percepcao
        if self._elementos != percepcao.elementos:#verifica se os elementos sao os elementos das percepcoes atuais
            self._elementos = percepcao.elementos #os elementos tornam se a percepcao desses elementos
            #self._estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            for posicao in percepcao.posicoes: #percorre todas as percepoes 
                self._estados.append(EstadoAgente(posicao)) #atualiza o estado, consoante as noves posicoes do agente
            self._alterado = True #alterado fica a true
        else:
            self._alterado = False #caso nao seja, nao altera (false)

    def estado(self):
        return self._estado

    def estados(self):
        return self._estados

    def operadores(self):
        return self._operadores

    """
    Metodo que obtem o elemento do dicionario de elementos, quando 
    uma key e igual a um estado'
    """
    def obter_elem(self,estado):
        for key in self.elementos.keys():
            if key == estado:
                return self.elementos[key]        

    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self._elementos)
        vista.marcar_posicao(self._estado.posicao)
        
    @property
    def elementos(self):
        return self._elementos 

    @property
    def alterado(self):
        return self._alterado

    

