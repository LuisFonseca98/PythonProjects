
"""
Classe que corresponde ao processo de decisao markov

Problema de decisao ao longo do tempo
->Utlidade de uma acao depende de uma sequencia de decisoes
->Possibilidade de ganhos e perdas
->Incerteza na decisao
->Efeito cumulativo

Um processo estocastico tem a proprieade de markov se a distruicao
probabilistica condicional dos estados futuros de um processo depender
exclusivamente do estado presente

A previsao dos estados seguintes so depende do estado presente

"""
class PDM:

    """
    Construtor que inicializa o valor do gama e delta max
    """
    def __init__(self,modelo,gama,delta_max):
        self._gama = gama #taxa de desconto para recompensas diferidas no tempo
        self._delta_max = delta_max
        self._modelo = modelo

    """
    Metodo que corresponde ao conceito de utilidade
    Efeito cumulativo da evolução da situação
    Historia de evolucao h (sequencia de estados)

    Recompensa
    -> Ganho ou perda num determinado estado
    -> Valor finito positivo ou negativo
    """
    def utilidade(self):
        U = {s:0 for s in self._modelo.S()}
        print("Inicio do calculo da Utilidade")
        while True:
            uAnterior = U.copy()
            delta = 0
            for s in self._modelo.S():
                print("a calcular a utilidade.......")
                U[s] = max([self.util_accao(s, a, uAnterior) for a in self._modelo.A(s)], default=0)
                delta = max(delta,abs(U[s] - uAnterior[s]))
            if delta <= self._delta_max: break
        print("Fim do calculo da utilidade")
        return U #retorno o valor da utilidade no final

    """
    Metodo que retorna a soma da utilidade segundo uma acao
    """
    def util_accao(self,s,a,U):
        return sum (p * self._modelo.R(s, a, sn) + self._gama * U[sn]
         for (p, sn) in self._modelo.T(s, a))

    """
    Metodo que calcula a politica
    """
    def politica(self,U):
        politica = {}
        for s in self._modelo.S():
            if self._modelo.A(s) != []:
                politica[s] = max(self._modelo.A(s), key = lambda a:self.util_accao(s,a,U))
        return politica
    
    """
    Metodo que resolve o PDM
    """
    def resolver(self):
        utilidade = self.utilidade()
        politica = self.politica(utilidade)
        return utilidade, politica