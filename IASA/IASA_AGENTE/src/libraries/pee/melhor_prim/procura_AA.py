

"""
Classe que corresponde  a procura A*

Esta procura corresponde a uma das tres variantes principais da
procura melhor primeiro

f(n) = g(n) + h(n), minimiza o custo global

Este tipo de procura é completo e otimo

Se os nos ja visitados nao forem eliminados, a heuristica
pode nao ser consistente

Uma heuristica consistente e tambem admissivel, no entanto
uma heuristica admissivel pode nao ser consistente

Mesmo se os nos ja visitados forem eliminados, existe a reducao 
da complexidade da procura

"""


from pee.melhor_prim.aval.aval_aa import AvalAA
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):

    """
    Método que inicia o avaliador da procura A*

    A heuristica admissivel segue as seguintes regras:
    -> 0 < h(n) < h*(n)
    -> h*(n): representa o custo minimo do no ate ao objectivo (percurso otimo)
    
    Uma heuristica admissivel e otimista, pois a estimativa de custo e sempre inferior
    ou igual ao custo efetivo minimo

    Se h(n) for consistente os valores de f(n) nunca diminuem ao longo de um caminho

    Para uma heuristica consistente:
    ->Sempre que e expandido um no o percurso desse no e otimo
    ->Sao expandidos todos os nos com f(n) < C*
    ->Sao eventualmente expandidos nos com f(n) = C* antes do no objectivo
    
    Metodo de procura de eficiencia otima para qualquer funcao heuristica:
    -> Nenhum outro algoritmo expandira menos nos, mantendo as caracteristicas de ser completo e otimo
    excepto nas situcoes entre nos com f(n) = C*

    No entanto nao resolve o problema da complexidade combinatoria, pois:
    -> o numero de nos expandidos dentro do contorno do no objetivo continua a ser uma funcao
    exponencial da dimensao do percurso ate ao objectivo
    -> a funcao heuristica afeta o contorno de procura: pode nao ser suficiente
    
    """
    def iniciar_avaliador(self):
        return AvalAA(self._heuristica)
