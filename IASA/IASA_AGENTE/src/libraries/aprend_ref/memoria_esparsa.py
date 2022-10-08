

from aprend_ref.memoria_aprend import MemoriaAprend

"""
Classe que representa a memoria esparsa
Esparsa: contem poucos valores de zero
"""
class MemoriaEsparsa(MemoriaAprend):
    """
    Construtor que recebe um valor por omissao
    conhece uma memoria e um conjunto de estados
    """
    def __init__(self,valor_omissao = 0.0):
        self._valor_omissao = valor_omissao
        #dicionario que recebe um tuplo <(Estado,Accao),double(valor do tuplo)>. Caso nao encontre nenhum valor, o valor de omissao e 0
        self._memoria = {}
        #nao vai admitir estados repetidos (lista que nao admite duplicados) 
        self._estados = set() 
    
    """
    Metodo que obtem o valor de q 
    num determinado estado com uma determinada acao
    """
    def q(self, s, a):
        return self._memoria.get((s,a),self._valor_omissao)
        #if (s,a) is not None and (s,a) in self._memoria:
            #return self._memoria.get((s,a))
        #return self._valor_omissao

    """
    Metodo que atualiza o valor de q na memoria
    """
    def actualizar(self, s, a, q):
        self._memoria[(s,a)] = q
        self._estados.add(s)
    
    def obter_estados(self):
        return self._estados

    @property
    def memoria(self):
        return self._memoria