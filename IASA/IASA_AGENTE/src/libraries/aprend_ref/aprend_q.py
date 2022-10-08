

from aprend_ref.aprend_ref import AprendRef

"""
Classe que corresponde ao algoritmo Q-Learning
"""
class AprendQ(AprendRef):

    """
    Construtor que conhece os valores do alfa e gama
    herda os metodos da classe "aprendizam reforco"
    """
    def __init__(self, mem_aprend, sel_accao,alfa,gama):
        super().__init__(mem_aprend,sel_accao)
        self._alfa = alfa
        self._gama = gama
    
    """
    Metodo onde pode ser visto a implementacao do Algoritmo Q-Learning
    """
    def aprender(self, s, a, r, sn):
        an = self._sel_accao.accao_sofrega(sn) #buscar a accao seguinte
        valorQsa = self._mem_aprend.q(s,a) #Iniciar Q(s,a)
        valorQsnan = self._mem_aprend.q(sn,an) #estado seguinte para a accao seguinte
        valorQ = valorQsa + self._alfa * (r + self._gama * (valorQsnan - valorQsa)) #formula Q-learning
        self._mem_aprend.actualizar(s,a,valorQ) #actualizar Q