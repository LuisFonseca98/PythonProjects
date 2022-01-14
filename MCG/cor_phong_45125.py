from cor_rgb_45125 import CorRGB
from ponto_45125 import Ponto3D
from vetor_45125 import Vetor3D
from imagem_45125 import Imagem
from luz_45125 import LuzPontual

"""A classe CorPhong representa o modelo de iluminação de Phong. Permite
obter a cor RGB de um ponto, no espaço 3D, usando este modelo de
iluminação."""
class CorPhong:

    """Inicializa os atributos do objeto"""
    def __init__(self, k_ambiente, k_difusa, k_especular, brilho):
        self.k_ambiente = k_ambiente
        self.k_difusa = k_difusa
        self.k_especular = k_especular
        self.brilho = brilho
        
    """Retorna uma string constituída por CorPhong(ka, kd, ke, b)"""
    def __repr__(self):
        return 'CorPhong(' + str(self.k_ambiente) + ', ' + str(self.k_difusa) + ', ' + str(self.k_especular) + ', ' + str(self.brilho) + ')'

    """Retorna a cor RGB de um ponto no espaço 3D, produzida por uma fonte
        de iluminação. A cor é calculada de acordo com o modelo na secção 2, a
        partir de:
        luz - a fonte de iluminação;
        direcao_luz - o vetor que aponta para a luz, a partir do ponto;
        normal - a normal à face onde está o ponto;
        direcao_olho  - o vetor que aponta para o espectador (olho) a partir do ponto;
        sombra - o booleano que indica se o ponto está em sombra de outros objectos
        (True) ou se está iluminado diretamente (False)"""
    def get_cor_rgb(self, luz, direcao_luz, normal, direcao_olho, sombra):
        k_ambiente = self.k_ambiente
        k_difusa = self.k_difusa
        k_especular = self.k_especular
        brilho = self.brilho

        R = (direcao_luz) * (-1) + normal * Vetor3D.interno(normal, direcao_luz) * 2

        cor_ambiente  = LuzPontual.get_intensidade_ambiente(luz)  * k_ambiente
        cor_difusa    = LuzPontual.get_intensidade_difusa(luz)    * k_difusa    * Vetor3D.interno(normal, direcao_luz)
        cor_especular = LuzPontual.get_intensidade_especular(luz) * k_especular * Vetor3D.interno(direcao_olho, R)** brilho


        if (sombra == True):
            return cor_ambiente
        elif(Vetor3D.interno(normal,direcao_luz) < 0):
            return cor_ambiente 
        
        return cor_ambiente + cor_especular + cor_difusa

if __name__ =="__main__":
    
    # teste ao construtor
    material_k_ambiente = CorRGB(0.0, 0.0, 0.1)
    material_k_difusa = CorRGB(0.0, 0.0, 0.9)
    material_k_especular = CorRGB(1.0, 1.0, 1.0)
    material_brilho = 100.0
    material_cor = CorPhong(material_k_ambiente,
    material_k_difusa,
    material_k_especular,
    material_brilho)

    # teste a __repr__
    print(material_cor)

    # teste a get_cor_rgb
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_intensidade_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_intensidade_ambiente, luz_intensidade_difusa,
                     luz_intensidade_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    n_pontos = 100
    imagem = Imagem(100, 100)
    incremento = 0.02 # 2.0/100.0
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(100): # índice de linhas
        for n in range(100): # índice de colunas
            ponto = Ponto3D(-1.0 + n*incremento,
                            1.0 - m*incremento, 0)
            direcao_luz = (luz.get_posicao() - ponto).versor()
            direcao_olho = (olho - ponto).versor()
            cor = material_cor.get_cor_rgb(luz, direcao_luz, normal,
            direcao_olho, sombra)
            imagem.set_cor(m+1, n+1, cor)
    imagem.guardar_como_ppm("cor_phong.ppm")

    # teste adicional - parâmetros
    h = 60.0
    n_pontos = 120
    # teste adicional
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_i_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_i_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_i_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_i_ambiente, luz_i_difusa, luz_i_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    k_ambiente = CorRGB(0.0, 0.0, 0.0)
    k_difusa = CorRGB(0.0, 0.0, 0.0)
    k_especular = CorRGB(0.9, 0.9, 0.9)
    brilho = 100.0
    k_ambiente.set_hsv(h, 1.0, 0.1)
    k_difusa.set_hsv(h, 1.0, 0.8)
    cor_phong = CorPhong(k_ambiente,
                         k_difusa,
                         k_especular,
    brilho)
    imagem = Imagem(n_pontos, n_pontos)
    incremento = 2.0 / n_pontos
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(n_pontos): # índice de linhas
        for n in range(n_pontos): # índice de colunas
            ponto = Ponto3D(-1.0 + n*incremento,
            1.0 - m*incremento, 0)
            direcao_luz = (luz.get_posicao() - ponto).versor()
            direcao_olho = (olho - ponto).versor()
            cor = cor_phong.get_cor_rgb(luz, direcao_luz, normal,
            direcao_olho, sombra)
            imagem.set_cor(m+1, n+1, cor)
    imagem.guardar_como_ppm("cor_phong_adicional.ppm")

