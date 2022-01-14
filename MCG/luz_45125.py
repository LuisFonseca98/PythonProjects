from cor_rgb_45125 import CorRGB
from ponto_45125 import Ponto3D
"""A classe LuzPontual representa uma fonte de iluminação pontual (uma
    luz pontual), que ilumina em todas as direções. A intensidade de iluminação
    não depende da distância aos objetos."""
class LuzPontual:
    """Inicializa os atributos do objecto"""
    def __init__(self,posicao,intensidade_ambiente,intensidade_difusa,intensidade_especular):
        self.posicao = posicao
        self.intensidade_ambiente = intensidade_ambiente
        self.intensidade_difusa = intensidade_difusa
        self.intensidade_especular = intensidade_especular

    """Retorna uma string constituída por LuzPontual(string1, string2, string3, string4),
        onde string1, string2, string3 e string4 resultam da conversão dos atributos
        posicao, intensidade_ambiente, intensidade_difusa e intensidade_especular
        para string, respectivamente."""
    def __repr__(self):
        return "LuzPontual(Ponto3D(" + (str(self.posicao)) + " , " + (str(self.intensidade_ambiente)) + " , " + (str(self.intensidade_difusa)) + " , " + (str(self.intensidade_especular)) + ")"

    """Retorna a posicao da LuzPontual"""
    def get_posicao(self):
        return self.posicao

    """Retorna a intensidade ambiente da LuzPontual"""
    def get_intensidade_ambiente(self):
        return self.intensidade_ambiente

    """Retorna a intensidade difusa da LuzPontual"""
    def get_intensidade_difusa(self):
        return self.intensidade_difusa

    """Retorna a intensidade especular da LuzPontual"""
    def get_intensidade_especular(self):
        return self.intensidade_especular
    
    
if __name__ == "__main__":
    # teste ao construtor
    posicao = Ponto3D(1.0, 2.0, 3.0)
    i_ambiente = CorRGB(0.1, 0.2, 0.3)
    i_difusa = CorRGB(0.4, 0.5, 0.6)
    i_especular = CorRGB(0.7, 0.8, 0.9)
    luz = LuzPontual(posicao, i_ambiente, i_difusa, i_especular)

    # teste a __repr__
    print(luz)

    # teste a get_posicao
    print(luz.get_posicao())

    # teste a get_intensidade_ambiente
    print(luz.get_intensidade_ambiente())

    # teste a get_intensidade_difusa
    print(luz.get_intensidade_difusa())

    # teste a get_intensidade_especular
    print(luz.get_intensidade_especular())
