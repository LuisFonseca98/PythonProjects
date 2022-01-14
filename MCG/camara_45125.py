from vetor_45125 import *
from ponto_45125 import *
from matriz_45125 import *

"""A classe Camara representa uma câmara numa cena 3D. A renderização
da cena é obtida por projeção no plano de projeção da câmara."""
class Camara:
    """Inicializa todos os atributos do objeto."""
    def __init__(self,posicao,olhar_para,vertical,distancia_olho_plano_projecao,largura_retangulo_projecao,altura_retangulo_projecao,resolucao_horizontal,resolucao_vertical):
        self.posicao = posicao
        self.olhar_para = olhar_para
        self.vertical = vertical
        self.distancia_olho_plano_projecao = distancia_olho_plano_projecao
        self.largura_retangulo_projecao = largura_retangulo_projecao
        self.altura_retangulo_projecao = altura_retangulo_projecao
        self.resolucao_horizontal = resolucao_horizontal
        self.resolucao_vertical = resolucao_vertical
        eixo_z = (self.olhar_para - self.posicao).versor()
        self.eixo_z = eixo_z
        eixo_y = (self.vertical + eixo_z * (-1.0 * vertical.interno(eixo_z))).versor()
        self.eixo_y = eixo_y
        eixo_x = eixo_z.externo(eixo_y)
        self.eixo_x = eixo_x
        incremento_horizontal = largura_retangulo_projecao/resolucao_horizontal
        self.incremento_horizontal = incremento_horizontal
        incremento_vertical = altura_retangulo_projecao / resolucao_vertical
        self.incremento_vertical = incremento_vertical
        canto_superior_esquerdo_x = largura_retangulo_projecao * (-1) / 2.0 + incremento_horizontal / 2.0
        self.canto_superior_esquerdo_x = canto_superior_esquerdo_x
        canto_superior_esquerdo_y = altura_retangulo_projecao / 2.0 - incremento_vertical / 2.0
        self.canto_superior_esquerdo_y = canto_superior_esquerdo_y
        canto_superior_esquerdo_z = distancia_olho_plano_projecao
        self.canto_superior_esquerdo_z = canto_superior_esquerdo_z
        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, eixo_x.get_x())
        matriz.set_entrada(2, 1, eixo_x.get_y())
        matriz.set_entrada(3, 1, eixo_x.get_z())
        matriz.set_entrada(1, 2, eixo_y.get_x())
        matriz.set_entrada(2, 2, eixo_y.get_y())
        matriz.set_entrada(3, 2, eixo_y.get_z())
        matriz.set_entrada(1, 3, eixo_z.get_x())
        matriz.set_entrada(2, 3, eixo_z.get_y())
        matriz.set_entrada(3, 3, eixo_z.get_z())
        matriz.set_entrada(1, 4, posicao.get_x())
        matriz.set_entrada(2, 4, posicao.get_y())
        matriz.set_entrada(3, 4, posicao.get_z())
        matriz.set_entrada(4, 4, 1.0) 
        self.matriz = matriz

    def __repr__(self):
        """Retorna uma string com os atributos do objeto do tipo Camara."""
        return "Camara(" \
                + str(self.posicao) + ",\n" \
                + str(self.olhar_para) + ",\n" \
                + str(self.vertical) + ",\n" \
                + str(self.distancia_olho_plano_projecao) + ",\n" \
                + str(self.largura_retangulo_projecao) + ",\n" \
                + str(self.altura_retangulo_projecao) + ",\n" \
                + str(self.resolucao_horizontal) + ",\n" \
                + str(self.resolucao_vertical) + ",\n" \
                + str(self.eixo_x) + ",\n" \
                + str(self.eixo_y) + ",\n" \
                + str(self.eixo_z) + ",\n" \
                + str(self.incremento_horizontal) + ",\n" \
                + str(self.incremento_vertical) + ",\n" \
                + str(self.canto_superior_esquerdo_x) + ",\n" \
                + str(self.canto_superior_esquerdo_y) + ",\n" \
                + str(self.canto_superior_esquerdo_z) + ",\n" \
                + str(self.matriz) \
                + ")"
    """Retorna a posicao da camera"""
    def get_posicao(self):
        return self.posicao
    
    """Retorna a resolucao vertical da camera"""
    def get_resolucao_vertical(self):
        return self.resolucao_vertical
    
    """Retorna a resolucao horizontal da camera"""
    def get_resolucao_horizontal(self):
        return self.resolucao_horizontal

    """Retorna o ponto do espaço na linha "linha", coluna "coluna", do plano de
        projeção, com coordenadas no sistema de coordenadas da câmara.
        Os números de linha de coluna iniciam-se em 1."""
    def get_pixel_local(self,linha,coluna):
        pixel_x = self.canto_superior_esquerdo_x + (coluna - 1) * self.incremento_horizontal
        pixel_y = self.canto_superior_esquerdo_y - (linha - 1) * self.incremento_vertical
        pixel_z = self.canto_superior_esquerdo_z
        return Ponto3D(pixel_x,pixel_y,pixel_z)

    """Retorna o ponto ponto no sistema de coordenadas global (onde está inserida
        a câmara). Para tal, transforma o ponto ponto com a matriz de mudança
        de coordenadas matriz."""
    def local_para_global(self,ponto):
        X_local = ponto.get_x()
        Y_local = ponto.get_y()
        Z_local = ponto.get_z()
        matriz = Matriz(4,1)
        matriz.set_entrada(1,1,X_local)
        matriz.set_entrada(2,1,Y_local)
        matriz.set_entrada(3,1,Z_local)
        matriz.set_entrada(4,1,1.0) 

        matriz_transformada = self.matriz * matriz
        X_global = matriz_transformada.get_entrada(1,1)
        Y_global = matriz_transformada.get_entrada(2,1)
        Z_global = matriz_transformada.get_entrada(3,1)
        return Ponto3D(X_global,Y_global,Z_global)
    
    """Retorna o ponto do espaço na linha linha, coluna coluna, do plano de
        projeção, com coordenadas no sistema de coordenadas global, da cena 3D
        onde a câmara está inserida.
        Os números de linha de coluna iniciam-se em 1."""
    def get_pixel_global(self,linha,coluna):
        pixel_local = self.get_pixel_local(linha,coluna)
        pixel_global = self.local_para_global(pixel_local)
        return pixel_global
    
if __name__ == "__main__":
    # teste ao construtor
    posicao = Ponto3D(0.0, 0.0, 3.0)
    olhar_para = Ponto3D(0.0, 0.0, 0.0)
    vertical = Vetor3D(0.0, 1.0, 0.0)
    distancia_olho_plano_projecao = 2.0
    largura_retangulo_projecao = 2.0
    altura_retangulo_projecao = 2.0
    resolucao_horizontal = 5
    resolucao_vertical = 5
    camara = Camara(posicao, olhar_para, vertical, distancia_olho_plano_projecao,
    largura_retangulo_projecao, altura_retangulo_projecao,
    resolucao_horizontal, resolucao_vertical)


    # teste a __repr__
    print(camara)

    print("teste a get_posicao")
    # teste a get_posicao
    print(camara.get_posicao())

    print("teste a get_resolucao_vertical")
    # teste a get_resolucao_vertical
    print(camara.get_resolucao_vertical())

    print("teste a get_resolucao_horizontal")
    #teste a get_resolucao_vertical
    print(camara.get_resolucao_vertical())

    # teste a get_pixel_local
    print(" ")
    print("sistema de coordenadas LOCAL")
    print("canto superior esquerdo = ")
    p1 = camara.get_pixel_local(1, 1)
    print(p1)
    print("canto superior direito = ")
    p2 = camara.get_pixel_local(1, 5)
    print(p2)
    print("canto inferior esquerdo = ")
    p3 = camara.get_pixel_local(5, 1)
    print(p3)
    print("canto inferioror direito = ")
    p4 = camara.get_pixel_local(5, 5)
    print(p4)

    # teste a local_para_global
    print(" ")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p1_global = camara.local_para_global(p1)
    print(p1_global)
    print("canto superior direito = ")
    p2_global = camara.local_para_global(p2)
    print(p2_global)
    print("canto inferior esquerdo = ")
    p3_global = camara.local_para_global(p3)
    print(p3_global)
    print("canto inferior direito = ")
    p4_global = camara.local_para_global(p4)
    print(p4_global)

    # teste a get_pixel_global
    print(" ")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p5 = camara.get_pixel_global(1, 1)
    print(p5)
    print("canto superior direito = ")
    p6 = camara.get_pixel_global(1, 5)
    print(p6)
    print("canto inferior esquerdo = ")
    p7 = camara.get_pixel_global(5, 1)
    print(p7)
    print("canto inferioror direito = ")
    p8 = camara.get_pixel_global(5, 5)
    print(p8)
