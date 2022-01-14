from vetor_45125 import Vetor3D
from ponto_45125 import Ponto3D
from reta_45125 import Reta
from matriz_45125 import Matriz
TOLERANCIA_ZERO = 10.0**(-10)
"""A classe Plano representa um plano. A classe ErroPontosColineares é
uma exceção (deriva de Exception) que é lançada quando se tenta definir
um plano com três pontos colineares ou coincidentes."""
class ErroPontosColineares(Exception):
    """exception"""
    
class Plano:
    """Inicializa os atributos do objecto,Caso o utilizador tente definir um plano com três pontos colineares (ou
        coincidentes) é lançada a exceção ErroPontosColineares. Considera-se que
        os pontos são colineares se o comprimento do produto externo referido no
        parágrafo anterior, antes de normalizado, for menor que (10.0)**−10
"""
    def __init__(self,ponto1,ponto2,ponto3):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3


        VetorP1_P2 = Ponto3D.subtrai_ponto(ponto2,ponto1)
        VetorP1_P3 = Ponto3D.subtrai_ponto(ponto3,ponto1)
        vetor_normal = Vetor3D.externo(VetorP1_P2,VetorP1_P3)
        
        if(vetor_normal.comprimento() <= TOLERANCIA_ZERO):
            raise ErroPontosColineares
        else:
            self.normal = vetor_normal.versor()
    """Retorna uma string constituída por Plano(p1, p2, p3, n), onde p1,
    p2 e p3 são as strings que resultam da conversão dos atributos ponto1, ponto2
    e ponto3, respetivamente, para string. n é a string que resulta da conversão
    para string do atributo normal"""
    def __repr__(self):
        return "Plano(" + str(self.ponto1) + str(self.ponto2) + str(self.ponto3) + str(self.normal) + ")"

    """Este método determina se a reta reta interceta o plano dentro do triângulo
    definido pelos atributos ponto1, ponto2 e ponto3, com parâmetro
    t > TOLERANCIA_ZERO. Caso intercete, calcula o ponto de interceção e o
    parâmetro da reta correspondente ao ponto de interceção.
    Retorna uma lista com 3 elementos."""
    def interceta_triangulo(self,reta):
        Ax = self.ponto1.x
        Ay = self.ponto1.y
        Az = self.ponto1.z

        Bx = self.ponto2.x
        By = self.ponto2.y
        Bz = self.ponto2.z

        Cx = self.ponto3.x
        Cy = self.ponto3.y
        Cz = self.ponto3.z

        Vx = reta.get_vetor_diretor().x
        Vy = reta.get_vetor_diretor().y
        Vz = reta.get_vetor_diretor().z

        Ox = reta.get_origem().x
        Oy = reta.get_origem().y
        Oz = reta.get_origem().z
        
        #Passo1 - calculo do valor absoluto do determinante
        M = Matriz(3,3)
        M.set_linha(1,[Ax-Bx,Ax-Cx,Vx])
        M.set_linha(2,[Ay-By,By-Cy,Vy])
        M.set_linha(3,[Az-Bz,Az-Cz,Vz])
        det_Matriz = M.det()

        if abs(det_Matriz) < TOLERANCIA_ZERO:
            return [False, None, None]

        #Passo2 - calcular a variavel t
        M1 = Matriz(3,3)
        M1.set_linha(1,[Ax-Bx,Ax-Cx,Ax-Ox])
        M1.set_linha(2,[Ay-By,Ay-Cy,Ay-Oy])
        M1.set_linha(3,[Az-Bz,Az-Cz,Az-Oz])
        t = M1.det()/det_Matriz
        

        if(t < TOLERANCIA_ZERO):
            return [False,None,None]

        #Passo3 - calculo da variavel tB
        M2= Matriz(3,3)
        M2.set_linha(1,[Ax-Ox,Ax-Cx,Vx])
        M2.set_linha(2,[Ay-Oy,Ay-Cy,Vy])
        M2.set_linha(3,[Az-Oz,Az-Cz,Vz])

        tB = M2.det()/det_Matriz
        if tB < 0.0 or tB >1.0:
            return [False,None,None]

        #Passo4 calculo da variavel tC
        M3 = Matriz(3,3)
        M3.set_linha(1,[Ax-Bx,Ax-Ox,Vx])
        M3.set_linha(2,[Ay-By,Ay-Oy,Vy])
        M3.set_linha(3,[Az-Bz,Az-Oz,Vz])
        tC = M3.det()/det_Matriz
        
        if tC < 0.0 or tC > 1.0:
            return [False,None,None]

        #Passo5 - Calculo da coordenada baricentrica
        tA = 1.0 - tB - tC
        if tA < 0.0 or tA>1.0:
            return [False,None,None]

        #Passo6 - Calcular o ponto de intersecao
        A = self.ponto1
        B = self.ponto2
        C = self.ponto3
        ponto_intercecao= A + (B-A) * tB + (C-A)*tC
        return [True,ponto_intercecao,t]
    
if __name__ == '__main__':
    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(2.0, 0.0, 0.0)
    c = Ponto3D(0.0, 2.0, 0.0)
    plano1 = Plano(a, b, c)
    print("Até aqui não foram lançadas exceções.")

    # teste a TOLERANCIA_ZERO
    print("TOLERANCIA_ZERO = " + str(TOLERANCIA_ZERO))

    # teste à exceção ErroPontosColineares
    try:
        plano2 = Plano(a, b, b)
    except ErroPontosColineares:
        print("Ao tentar definir-se o plano plano2 = Plano(a, b, b)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("A execução foi interrompida. plano2 não ficou definida.")

    # teste a __repr__
    # a normal tem que apontar no sentido do eixo dos z’s
    # e tem que ter comprimento 1
    print(plano1)

   # testes a interceta_triangulo
    p1 = Ponto3D(1.0, 1.0, 10.0)
    p2 = Ponto3D(1.0, 1.0, 5.0)
    r1 = Reta(p1, p2)
    trio = plano1.interceta_triangulo(r1)
    if trio[0] == True:
        print("r1 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
        print("interceção calculada com a equação da reta e t.")
        print("(tem que dar o mesmo que trio[1])")
        t = trio[2]
        pi = r1.get_origem() + (r1.get_vetor_diretor() * t)
        print(pi)
    else:
        print("r1 NÃO interceta plano1.")
    p3 = Ponto3D(2.0, 2.0, 10.0)
    r2 = Reta(p1, p3)
    trio = plano1.interceta_triangulo(r2)
    if trio[0] == True:
        print("r2 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
    else:
        print("r2 NÃO interceta plano1.")
