from vetor_45125 import Vetor3D
"""A classe Ponto3D representa um ponto num espaço com 3 dimensões.
Suporta as operações elementares de cálculo vetorial.
"""
class Ponto3D:
    """Inicializa os atributos do objecto"""
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    """Retorna a coordenada x do ponto"""
    def get_x(self):
        return self.x
    """Retorna a coordenada y do ponto"""
    def get_y(self):
        return self.y
    """Retorna a coordenada z do ponto"""
    def get_z(self):
        return self.z
    
    """Retorna uma string constituída por Ponto3D(valorx, valory, valorz),
        onde valorx, valorx e valory são as coordenadas do ponto.
"""
    def __repr__(self):
        return "Ponto3D(" + str(self.x) +"," + str(self.y) +"," + str(self.z) + ")"
    """Retorna um novo ponto que resulta da translação do ponto self com o
    vetor um_vetor"""
    def adiciona_vetor(self,um_vetor): 
        return Ponto3D(self.x + um_vetor.x, self.y + um_vetor.y, self.z + um_vetor.z)
    """É a função chamada pelo interpretador de Python quando o operador +
        é executado sobre um objeto Ponto3D.
        Retorna um novo ponto que resulta da translação do ponto self com o
        vetor um_vetor."""
    def __add__(self,um_vetor):
        return self.adiciona_vetor(um_vetor)
    """Retorna um objecto da classe Vetor3D, que representa a translação que
        aplicada ao ponto ponto_inicial"""
    def subtrai_ponto(self,ponto_inicial): 
        return Vetor3D(self.x - ponto_inicial.x, self.y - ponto_inicial.y, self.z - ponto_inicial.z)
    """É a função chamada pelo interpretador de Python quando o operador -
        é executado sobre um objeto Ponto3D.
        Retorna um novo ponto que resulta da translação do ponto self com o
        vetor um_vetor."""
    def __sub__(self,ponto_inicial):
        return self.subtrai_ponto(ponto_inicial)
    
############################TESTES#######################
if __name__ == "__main__":
    # teste ao construtor
    p1 = Ponto3D(1.0, 2.0, 3.0)

    # teste a get_x
    print("coordenada x de p1 = ")
    print(p1.get_x())

    # teste a get_y
    print("coordenada y de p1 = ")
    print(p1.get_y())

    # teste a get_z
    print("coordenada z de p1 = ")
    print(p1.get_z())

    # teste a __repr__
    print("p1 = ")
    print(p1)

    # teste a adiciona_vetor
    v1 = Vetor3D(10.0, 20.0, 30.0)
    p2 = p1.adiciona_vetor(v1)
    print("v1 = ")
    print(v1)
    print("p2 = ")
    print(p2)

    # teste a +
    p3 = p1 + v1
    print("p3 = p1 + v1 = ")
    print(p3)

    # teste a subtrai_ponto
    v2 = p2.subtrai_ponto(p1)
    print("v2 = ")
    print(v2)

    # teste a -
    v3 = p2 - p1
    print("v3 = ")
    print(v3)

