from ponto_45125 import *
from cor_rgb_45125 import *
from plano_45125 import *
from reta_45125 import *
from cor_phong_45125 import *
from vetor_45125 import *

"""A classe FaceTriangular representa as faces triangulares dos objetos
numa cena 3D. A classe FaceTriangular é um plano definido com 3 pontos,
que tem uma cor Phong de forma a imitar um material. Como uma face
triangular é um plano, a classe FaceTriangular deriva da classe Plano, e
tem um atributo adicional que representa a cor Phong."""

class FaceTriangular(Plano):
    """A chamada à função super() retorna o objeto da classe base, neste caso,
        o objeto da classe Plano.
        Inicializa ainda o atributo cor_phong com o argumento correspondente."""
    def __init__(self,ponto1,ponto2,ponto3,cor_phong):
        super().__init__(ponto1,ponto2,ponto3)
        self.cor_phong = cor_phong
    """Retorna uma string constituída por FaceTriangular(plano, cor), onde
        plano é a string que resulta da chamada à função __repr__ da classe base e
        cor é a string que resulta da conversão do atributo cor_phong para string.
        A chamada à função __repr__ da classe base é feita recorrendo novamente
        à função super"""
    def __repr__(self):
        return "FaceTriangular(" + str(super().__repr__()) + str(self.cor_phong) + ")"
    
    """Retorna o atributo corPhong"""
    def get_cor_phong(self):
        return self.cor_phong

if __name__ =="__main__":
    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(1.0, 0.0, 0.0)
    c = Ponto3D(0.0, 1.0, 0.0)
    k_ambiente = CorRGB(0.0, 0.0, 0.1)
    k_difusa = CorRGB(0.0, 0.0, 0.75)
    k_especular = CorRGB(1.0, 1.0, 1.0)
    brilho = 100.0
    cor = CorPhong(k_ambiente, k_difusa, k_especular, brilho)
    face1 = FaceTriangular(a, b, c, cor)
    print("Até aqui não foram lançadas exceções.")

    # teste à exceção ErroPontosColineares
    try:
        face2 = FaceTriangular(a, a, c, cor)
    except ErroPontosColineares:
        print("Ao tentar definir-se a face face2 = FaceTriangular(a, a, c, cor)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("É o comportamento herdado da classe Plano.")

    #teste a __repr__
    print(face1)

    # teste a get_cor_phong
    print(face1.get_cor_phong())
