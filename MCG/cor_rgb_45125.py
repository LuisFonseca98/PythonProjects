from colorsys import hsv_to_rgb

"""Representa a class CorRGB(Red,Green,Blue)"""
class CorRGB:
    """Fornece-se os atributos r(red), g(green) e b(blue), a variar entre um valor mínimo(0.0) e um valor máximo(1.0)"""
    def __init__(self,red,green,blue):
       self.r=max(min(red,1.0),0.0)
       self.g=max(min(green,1.0),0.0)
       self.b=max(min(blue,1.0),0.0)

    """Função repr(deriva da abreviatura represation)usada para representar os atributos, usando a string"""
    def __repr__(self):
        return str(int(self.r*255.0)) + " " + str(int(self.g*255.0)) + " " + str(int(self.b*255.0))
    """Funo que faz a soma das três cores"""
    def soma(self,outra_cor):
        return CorRGB(self.r+outra_cor.r,self.g+outra_cor.g,self.b+outra_cor.b)
    
    """Função quando o operador + é executado sobre um objecto da CorRGB"""
    def __add__(self,outra_cor):
        return self.soma(outra_cor)

    """Função no qual se especifica uma cor a partir dos componentes hue, saturation e value"""
    def set_hsv(self,h,s,v):
        (self.r,self.g,self.b) = hsv_to_rgb(h/360.0,s,v)
        return self

    """Função onde se faz a operação multiplicação das três cores"""
    def multiplica(self,outra_cor):
        return CorRGB(self.r*outra_cor.r,self.g*outra_cor.g,self.b*outra_cor.b)

    """Função de multiplica das coresRCG por um escalar(número)"""
    def multiplica_escalar(self,escalar):
        return CorRGB(self.r*escalar,self.g*escalar,self.b*escalar)

    """Função quando o operador * e executado sobre um objecto da corRGB"""
    def __mul__(self,valor):
        if isinstance(valor,float):
            return self.multiplica_escalar(valor)
        else:
            return self.multiplica(valor)
if __name__ == "__main__":
    # testes ao construtor
    c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
    c2 = CorRGB(0.0, 1.0, 0.0) # verde
    c3 = CorRGB(0.0, 0.0, 1.0) # azul
    c4 = CorRGB(1.0, 1.0, 1.0) # branco
    c5 = CorRGB(0.0, 0.0, 0.0) # preto

    # testes ao método __repr__
    print("repr")
    c1 = CorRGB(1.0, 0.0, 0.0)
    print(c1)
    print("c1 = " + str(c1))

    print("teste adicional ao repr")
    # mais testes ao construtor
    c2 = CorRGB(-0.1, 0.1, 1.1)
    print(c2)

    print("teste adicional ao repr")
    # mais testes ao método __repr__
    lista = [c1, c2]
    print(lista)

    print("teste soma")
    # testes ao método soma
    c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
    c2 = CorRGB(0.0, 1.0, 0.0) # verde
    c3 = CorRGB(1.0, 1.0, 1.0) # branco
    c4 = c1.soma(c2)
    c5 = c1.soma(c3)
    print(c4)
    print(c5)

    print("teste ao +")
    # testes ao operador +
    c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
    c2 = CorRGB(0.0, 1.0, 0.0) # verde
    c3 = CorRGB(1.0, 1.0, 1.0) # branco
    c4 = c1 + c2
    c5 = c1 + c3
    print(c4)
    print(c5)


    print("set_hsv")
    # testes ao método set_hsv
    c1 = CorRGB(0.0, 0.0, 0.0)
    c1.set_hsv(360.0, 1.0, 1.0)
    print(c1)

    print("multiplica")
    # testes ao método multiplica
    c1 = CorRGB(1.0, 0.0, 0.0)
    c2 = CorRGB(1.0, 1.0, 1.0)
    c3 = CorRGB(0.0, 0.0, 0.0)
    c4 = c1.multiplica(c2)
    c5 = c1.multiplica(c3)
    print(c4)
    print(c5)

    print("multiplica_escalar")
    # testes ao método multiplica_escalar
    c1 = CorRGB(1.0, 1.0, 1.0)
    e1 = 0.0
    e2 = 0.5
    e3 = 1.0
    e4 = 2.0
    c2 = c1.multiplica_escalar(e1)
    c3 = c1.multiplica_escalar(e2)
    c4 = c1.multiplica_escalar(e3)
    c5 = c1.multiplica_escalar(e4)
    print(c2)
    print(c3)
    print(c4)
    print(c5)

    # testes ao operador *
    print("operador * ")
    c1 = CorRGB(1.0, 1.0, 1.0)
    c2 = CorRGB(0.0, 0.5, 1.0)
    e1 = 0.5
    c3 = c1 * c2 # segundo operando do tipo CorRGB
    c4 = c1 * e1 # segundo operando do tipo float (um escalar)
    print(c3)
    print(c4)

