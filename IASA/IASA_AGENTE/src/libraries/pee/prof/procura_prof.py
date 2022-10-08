"""
Classe que representa a procura em profundidade
"""

from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
A Procura em Profundidade e aquela procura que percorre os nós até chegar a um limite imposto pelo utilizador
enquanto esse limite não é atingido ao chegarmos a um novo nó é preciso realizar a sua expansão
para que se possa executar o passo seguinte.

Assim sendo, é verificado se a profundidade do nó atual é maior que o limite imposto, caso a 
a profundidade do nó já tenha ultrapassado a profundidade limite, é retornado None pois não
foi encontrada nenhuma solução para o problema.

Caso ainda não se tenha atingido a profundidade limite é verificado se a procura se encontra num 
ciclo ou seja se vai repetida infinitamente, caso não seja esse o caso é chamada a expansão
da classe MecanismoProcura e é realizada a expansão do nó
    
"""

class ProcuraProf(MecanismoProcura):

    def _iniciar_fronteira(self):
        return FronteiraLIFO()

    def _memorizar(self, no):
        self._fronteira.inserir(no)
