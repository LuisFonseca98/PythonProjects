class Vetor3D:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __repr__(self):
        return "Vetor3D:(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def adiciona(self,outro_vetor):
        return Vetor3D(self.x + outro_vetor.x, self.y + outro_vetor.y, self.z + outro_vetor.z)

    def __add__(self,outro_vetor):
        return self.adiciona(outro_vetor)

    def multiplica_escalar(self,escalar):
        return Vetor3D(self.x * escalar, self.y * escalar, self.z * escalar)

    def __mul__(self,escalar):
        return (self.multiplica_escalar(escalar))

    def comprimento(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def versor(self):
        vetor2 = 1.0/self.comprimento()
        return self*vetor2

    def interno(self,outro_vetor):
        return self.x*outro_vetor.x + self.y*outro_vetor.y + self.z*outro_vetor.z
    
    def externo(self,outro_vetor):
        e1 = self.y*outro_vetor.z - self.z*outro_vetor.y
        e2 = -(self.x*outro_vetor.z - self.z*outro_vetor.x)
        e3 = self.x*outro_vetor.y - self.y*outro_vetor.x
        return Vetor3D(e1,e2,e3)

###############################################TESTES##################
if __name__== '__main__':
    # teste ao construtor
    v1 = Vetor3D(1.0, 2.0, 3.0)

    # teste a get_x
    print("get_x")
    print("coordenada x de v1 = ")
    print(v1.get_x())
    
    print("get_y")
    # teste a get_y
    print("coordenada y de v1 = ")
    print(v1.get_y())

    print("get_z")
    # teste a get_z
    print("coordenada z de v1 = ")
    print(v1.get_z())

    print("teste a repr")
    # teste a __repr__
    print("v1 = ")
    print(v1)

    print("adiciona")
    # teste a adiciona
    v2 = Vetor3D(10.0, 20.0, 30.0)
    v3 = v1.adiciona(v2)
    print("v1 = ")
    print(v1)
    print("v2 = ")
    print(v2)
    print("v3 = ")
    print(v3)

    print("teste a +")
    # teste a +
    v4 = v1 + v2
    print("v4 = ")
    print(v4)

    print("multiplica_escalar")
    # teste a multiplica_escalar
    a = 2.0
    v5 = v1.multiplica_escalar(a)
    print("v5 = ")
    print(v5)

    print("teste a * ")
    # teste a *
    v6 = v1 * a
    print("v6 = ")
    print(v6)

    print("teste a comprimento")
    # teste a comprimento
    v7 = Vetor3D(3.0, 0.0, 4.0)
    cv7 = v7.comprimento()
    print("v7 = ")
    print(v7)
    print("comprimento de v7 = ")
    print(cv7)

    print("teste a versor")
    # teste a versor
    vv7 = v7.versor()
    cvv7 = vv7.comprimento()
    print("vv7 = ")
    print(vv7)
    print("comprimento de vv7 = ")
    print(cvv7)

    print("teste a interno")
    # teste a interno
    print("v1 =")
    print(v1)
    print("v7 =")
    print(v7)
    iv1v7 = v1.interno(v7)
    print("v1 interno v7 = ")
    print(iv1v7)

    print("teste a externo")
    # teste a externo
    e = v1.externo(v7)
    print("e = v1 externo v7 = ")
    print(e)
    
    print("teste a interno")
    print("v1 interno e = ")
    print(v1.interno(e))
    print("v7 interno e = ")
    print(v7.interno(e))
