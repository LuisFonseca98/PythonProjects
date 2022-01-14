
from cor_rgb_45125 import CorRGB
from io import StringIO

"""A classe Imagem armazena uma imagem RGB, permite especificar a cor
de cada pixel, permite obter a cor de cada pixel, e permite gravar a imagem
em formato .ppm.
"""

class Imagem:
    """Função onde se inicializa os atributos numero_linhas e numero_colunas,os atributos numero_linhas e numero_colunas armazenam o número de
    linhas e o número de colunas da imagem, respetivamente """

    def __init__(self, numero_linhas, numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas=[]
        for l in range (numero_linhas):
            linha =[]
            for c in range(numero_colunas):
                linha.append(CorRGB(0,0,0))
            self.linhas.append(linha)
    """Função usada para retornar os atributos inicializados em string, usando um objecto da classe io.StringIO"""
    def __repr__(self):
        str_din=StringIO()
        str_din.write("P3\n")
        str_din.write("# imagem criada por mcg/leim/isel\n")
        str_din.write(str(self.numero_colunas)+" " +str(self.numero_linhas) + "\n")
        str_din.write("255\n")
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                pixel_str = str(self.linhas[l][c])
                str_din.write(pixel_str + " ")
            str_din.write("\n")
        resultado = str_din.getvalue()
        str_din.close()
        return resultado

    """Função que substitui o pixel na linha "linha", coluna "coluna" pelo pixel cor_rgb."""
    def set_cor(self,linha,coluna,cor_rgb):
        self.linhas[linha - 1][coluna - 1] = cor_rgb

    """Função que retorna o pixel na linha "linha", coluna "coluna" """
    def get_cor(self,linha,coluna):
        return self.linhas[linha - 1][coluna - 1]

    """Função que Abre o ficheiro em modo de escrita, escreve no ficheiro a representação
       PPM ASCII da imagem RGB e fecha o ficheiro """
    def guardar_como_ppm(self,nome_ficheiro):
        ficheiro = open(nome_ficheiro, 'w')
        ficheiro.write(str(self))
        ficheiro.close
        
## TESTES
if __name__ == "__main__":

    # teste ao construtor
    imagem1 = Imagem(5, 5)

    print("teste a repr")
    # teste a __repr__
    imagem2 = Imagem(5, 5)
    print(imagem2)

    print("teste a set_cor")
    # teste a set_cor
    imagem3 = Imagem(5, 5)
    branco = CorRGB(1.0, 1.0, 1.0)
    imagem3.set_cor(3, 3, branco)
    print(imagem3)

    print("teste a get_cor")
    # testes a get_cor
    imagem4 = Imagem(5, 5)
    branco = CorRGB(1.0, 1.0, 1.0)
    imagem4.set_cor(3, 3, branco)
    print(imagem4.get_cor(3, 3))
    print(imagem4.get_cor(5, 5))

    print("teste a guardar como ppm")
    # teste a guardar_como_ppm
    imagem5 = Imagem(3, 5)
    red = CorRGB(1.0, 0.0, 0.0)
    green = CorRGB(0.0, 1.0, 0.0)
    blue = CorRGB(0.0, 0.0, 1.0)
    imagem5.set_cor(2, 2, red)
    imagem5.set_cor(2, 3, green)
    imagem5.set_cor(2, 4, blue)
    imagem5.guardar_como_ppm("imagem5.ppm")

    print("------------------Imagem Adicional-----------------")
    # teste adicional
    linhas = 100
    colunas = 200
    imagem6 = Imagem(linhas, colunas)
    h = 130.0
    incremento_s = 1.0 / (colunas - 1)
    incremento_v = 1.0 / (linhas - 1)
    for l in range(linhas):

        v = l * incremento_v
        for c in range(colunas):
            s = c * incremento_s
            pixel = CorRGB(0.0, 0.0, 0.0)
            pixel.set_hsv(h, s, v)
            imagem6.set_cor(l+1, c+1, pixel)
    imagem6.guardar_como_ppm("imagem6.ppm")
