from io import StringIO

"""Os atributos numero_linhas e numero_colunas armazenam o número de
linhas e o número de colunas da matriz.
O atributo linhas é uma lista com numero_linhas elementos, que armazena
as linhas da matriz.
Cada elemento da lista linhas, é, por sua vez, uma lista com numero_colunas
entradas da matriz. As entradas são números."""

class Matriz:
    """Funcao onde se inicializa os atributos numero_linhas e numero_colunas"""
    def __init__(self,numero_linhas,numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas=[]
        for l in range(numero_linhas):
            linha=[]
            for c in range(numero_colunas):
                linha.append(0.0)
            self.linhas.append(linha)
    """Funcao que retorna os atributos em str"""
    def __repr__(self):
        resultado = ("Matriz(" + str(self.numero_linhas) + "," + str(self.numero_colunas) + ")\n")
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado=resultado+str(self.linhas[l][c])+" "
            resultado=resultado + "\n"
        return resultado

    """Funcao que substitui o valor da entrada da matriz na linha "linha", coluna "coluna" pelo valor "valor" """
    def set_entrada(self,linha,coluna,valor):
         self.linhas[linha - 1 ][coluna - 1] = valor
         return valor

    """Funcao que substitui o valor da entrada da matriz na linha "linha", coluna "coluna" pelo valor "valor" """
    def get_entrada(self,linha,coluna):
        return self.linhas[linha - 1][coluna - 1]

    """Funcao que retorna uma nova matriz igual à soma da matriz self com a matriz outra_matriz"""
    def adiciona(self,outra_matriz):
        soma = Matriz(self.numero_linhas,self.numero_colunas)
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                valor = 0.0
                valor = valor + self.linhas[l][c] + outra_matriz.linhas[l][c]
                soma.linhas[l][c] = valor
        return soma
    """Funcção usada quando o operador + é executado sobre um objeto Matriz"""
    def __add__(self,outra_matriz):
        return self.adiciona(outra_matriz)

    """Funcao que retorna uma nova matriz igual à multiplicação da matriz
        self pela matriz outra_matriz. O número de linhas da nova matriz é igual
        ao número de linhas da matriz self. O número de colunas da nova matriz é
        igual ao número de colunas da matriz outra_matriz"""
    def multiplica(self,outra_matriz):
        resultado = Matriz(self.numero_linhas,outra_matriz.numero_colunas)
        for l in range (resultado.numero_linhas):
           for c in range (resultado.numero_colunas):
               valor = 0.0
               for b in range(self.numero_colunas):
                   valor = valor + self.linhas[l][b]*outra_matriz.linhas[b][c]
               resultado.linhas[l][c] = valor
        return resultado

    """Funcao que retorna uma nova matriz igual à multiplicação da matriz self pelo escalar "escalar" """
    def multiplica_escalar(self,escalar):
        resultado = Matriz(self.numero_linhas,self.numero_colunas)
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado.linhas[l][c] = self.linhas[l][c] * escalar
        return resultado
    """Função usada quando o operador * é executado sobre um objecto Matriz"""
    def __mul__(self,valor):
        if isinstance(valor,float):
            return self.multiplica_escalar(valor)
        else:
            return self.multiplica(valor)
    """Função que retorna o valor do determinante de uma matriz de 2 por 2"""
    def det_2x2(self):
        return self.linhas[0][0] * self.linhas[1][1] - self.linhas[0][1] * self.linhas[1][0]

    """Função que retorna o valor do determinante de uma matriz de 3 por 3"""
    def det_3x3(self):
        #Calcular o determinate duma matriz 3x3, exemplo dessa mesma : 
        #A B C 
        #D E F 
        #G H I
         A = self.linhas[0][0]
         B = self.linhas[0][1]
         C = self.linhas[0][2]
         D = self.linhas[1][0]
         E = self.linhas[1][1]
         F = self.linhas[1][2]
         G = self.linhas[2][0]
         H = self.linhas[2][1]
         I = self.linhas[2][2]
         return A*E*I + B*F*G + C*D*H - C*E*G - F*H*A - I*B*D 
    """Função que retorna uma nova matriz que resulta da matriz self com a linha "linha_a_remover" e a coluna "coluna_a_remover" removidas"""
    def sub_matriz(self,linha_a_remover,coluna_a_remover):
        resultado = Matriz(self.numero_linhas-1,self.numero_colunas-1)
        for l in range(resultado.numero_linhas):
            for c in range(resultado.numero_colunas):
                lindex = l
                cindex = c
                if l >= linha_a_remover - 1:
                    lindex = l + 1
                if c >= coluna_a_remover - 1:
                    cindex = c + 1
                resultado.linhas[l][c] = self.linhas[lindex][cindex]
        return resultado

    """Função que retorna o valor do determinante de uma matriz quadrada de qualquer dimensão."""
    def det(self):
        if self.numero_linhas == 1:
            return self.linhas[0][0]
        elif self.numero_linhas == 2:
            return self.det_2x2()
        elif self.numero_linhas == 3:
            return self.det_3x3()
        else:
            resultado = 0.0
            for c in range(self.numero_colunas):
                resultado = resultado +(-1)**c*self.linhas[0][c]*self.sub_matriz(1,c+1).det()
        return resultado

    """Função que retorna uma nova matriz igual à matriz self transposta. Neste caso o numero_linhas vai ser igual ao número de colunas da matriz self,
       e o numero_colunas vai ser igual ao número de linhas da matriz outra_matriz"""
    def transposta(self):
        nova_matriz = Matriz(self.numero_colunas,self.numero_linhas)
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                nova_matriz.set_entrada(c,l,self.get_entrada(l,c))
        return nova_matriz

    """Função que retorna uma nova matriz que é uma cópia de self"""
    def copia(self):
        resultado = Matriz(self.numero_linhas,self.numero_colunas)
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado.set_entrada(c,l,self.get_entrada(c,l))
        return resultado

    """Função que copia os elementos da lista uma_lista para a linha "linha"
        da matriz self, pela mesma ordem. Retorna a propria matriz self"""
    def set_linha(self,linha,uma_lista):
        for c in range(self.numero_colunas):
            self.set_entrada(linha,c+1,uma_lista[c])
        return self
        
    """Função que copia os elementos da lista uma_lista para a coluna "coluna"
        da matriz self, pela mesma ordem. Retorna a propria matriz self"""
    def set_coluna(self,coluna,uma_lista):
        for l in range(self.numero_linhas):
            self.set_entrada(l+1,coluna,uma_lista[l])
        return self

#TESTES
if __name__ == "__main__":

    # teste ao construtor
    m1 = Matriz(3,4)
    print("teste ao repr")
    # teste a __repr__
    print(m1)

    # teste a set_entrada
    print("teste a set_entrada")
    m1.set_entrada(1, 2, 1.0)
    m1.set_entrada(2, 2, 2.0)
    m1.set_entrada(3, 2, 3.0)
    print(m1)

    # teste a get_entrada
    print("get_entrada")
    print("m1 entrada 3,1 = ")
    print(m1.get_entrada(3, 1))
    print("m1 entrada 3,2 = ")
    print(m1.get_entrada(3, 2))


    # teste a adiciona
    print("teste a adiciona")
    m2 = m1.adiciona(m1)
    print(m2)

    print("teste a +")
    # teste a +
    m3 = m1 + m1
    print(m3)

    print("teste a multiplica")
    # teste a multiplica
    m4 = Matriz(4, 3)
    m4.set_entrada(2, 1, 1.0)
    m4.set_entrada(2, 2, 2.0)
    m4.set_entrada(2, 3, 3.0)
    m5 = m1.multiplica(m4)
    print(m5)

    print("teste a multiplica_escalar")
    # teste a multiplica_escalar
    m5a = m5.multiplica_escalar(-1.0)
    print(m5a)

    print("teste a * ")
    # teste a *
    m6 = m1 * m4
    print(m6)
    m6a = m1 * 2.0
    print(m6a)

    # teste a det_2x2
    print("teste ao determinate 2x2")
    m7 = Matriz(2, 2)
    m7.set_entrada(1, 1, 1.0)
    m7.set_entrada(1, 2, 2.0)
    m7.set_entrada(2, 1, 3.0)
    m7.set_entrada(2, 2, 4.0)
    print(m7)
    print("det(m7) = " + str(m7.det_2x2()))

    print("teste ao determinate 3x3")
    # teste a det_3x3
    print(m6)
    print("det(m6) = " + str(m6.det_3x3()))

    print("teste a sub_matriz")
    # teste a sub_matriz
    m8 = m6.sub_matriz(2, 2)
    print(m8)

    print("teste a det")

    # testes a det
    print(m7.det())
    print(m6.det())
    m9 = Matriz(5, 5)
    m9.set_entrada(1, 1, 2.0)
    m9.set_entrada(2, 2, 2.0)
    m9.set_entrada(3, 3, 2.0)
    m9.set_entrada(4, 4, 2.0)
    m9.set_entrada(5, 5, 2.0)
    print(m9)
    print(m9.det())

    print("teste a transpota")
    # teste a transposta
    m1t = m1.transposta()
    print(m1t)

    print("teste a copia")
    # testes a copia
    print("copia")
    m10 = m8.copia()
    m10.set_entrada(1, 1, -2.0)
    print(m8)
    print(m10)

    #teste a set_linha
    print("set_linhas")
    m9.set_linha(5, [1.0, 2.0, 3.0, 4.0, 5.0])
    print(m9)

    # teste a set_coluna
    print("set_coluna")
    m9.set_coluna(3, [10.0, 20.0, 30.0, 40.0, 50.0])
    print(m9)
    print("-----------------------Teste Adicional-------------------------------")
    # teste adicional a determinantes de matrizes de 9x9
    matriz_A = Matriz(9, 9)
    matriz_A.set_linha(1, [4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 7.0, 0.0, 0.0])
    matriz_A.set_linha(2, [0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 7.0, 0.0])
    matriz_A.set_linha(3, [0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 7.0])
    matriz_A.set_linha(4, [6.0, 0.0, 0.0, 9.0, 0.0, 0.0, 8.0, 0.0, 0.0])
    matriz_A.set_linha(5, [0.0, 6.0, 0.0, 0.0, 9.0, 0.0, 0.0, 8.0, 0.0])
    matriz_A.set_linha(6, [0.0, 0.0, 6.0, 0.0, 0.0, 9.0, 0.0, 0.0, 8.0])
    matriz_A.set_linha(7, [1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0, 0.0])
    matriz_A.set_linha(8, [0.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0])
    matriz_A.set_linha(9, [0.0, 0.0, 1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 3.0])
    det_A = matriz_A.det()
    print("det(A) = " + str(det_A))
    lista_B = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    matriz_A1 = matriz_A.copia()
    matriz_A2 = matriz_A.copia()
    matriz_A3 = matriz_A.copia()
    matriz_A4 = matriz_A.copia()
    matriz_A5 = matriz_A.copia()
    matriz_A6 = matriz_A.copia()
    matriz_A7 = matriz_A.copia()
    matriz_A8 = matriz_A.copia()
    matriz_A9 = matriz_A.copia()
    matriz_A1.set_coluna(1, lista_B)
    matriz_A2.set_coluna(2, lista_B)
    matriz_A3.set_coluna(3, lista_B)
    matriz_A4.set_coluna(4, lista_B)
    matriz_A5.set_coluna(5, lista_B)
    matriz_A6.set_coluna(6, lista_B)
    matriz_A7.set_coluna(7, lista_B)
    matriz_A8.set_coluna(8, lista_B)
    matriz_A9.set_coluna(9, lista_B)
    a = matriz_A1.det()/det_A
    print("a = " + str(round(a, 3)))
    b = matriz_A2.det()/det_A
    print("b = " + str(round(b, 3)))
    c = matriz_A3.det()/det_A
    print("c = " + str(round(c, 3)))
    d = matriz_A4.det()/det_A

    print("d = " + str(round(d, 3)))
    e = matriz_A5.det()/det_A
    print("e = " + str(round(e, 3)))
    f = matriz_A6.det()/det_A
    print("f = " + str(round(f, 3)))
    g = matriz_A7.det()/det_A
    print("g = " + str(round(g, 3)))
    h = matriz_A8.det()/det_A
    print("h = " + str(round(h, 3)))
    i = matriz_A9.det()/det_A
    print("i = " + str(round(i, 3)))
    # verificação
    matriz_M = Matriz(3, 3)
    matriz_M.set_linha(1, [4.0, 5.0, 7.0])
    matriz_M.set_linha(2, [6.0, 9.0, 8.0])
    matriz_M.set_linha(3, [1.0, 2.0, 3.0])
    matriz_M_inversa = Matriz(3, 3)
    matriz_M_inversa.set_linha(1, [a, b, c])
    matriz_M_inversa.set_linha(2, [d, e, f])
    matriz_M_inversa.set_linha(3, [g, h, i])
    matriz_I = matriz_M * matriz_M_inversa
    print(matriz_I)
    print("Entradas de matriz_I com 3 casas decimais")
    print(str(round(matriz_I.get_entrada(1,1), 3)) + " "
    + str(round(matriz_I.get_entrada(1,2), 3)) + " "
    + str(round(matriz_I.get_entrada(1,3), 3)))
    print(str(round(matriz_I.get_entrada(2,1), 3)) + " "
    + str(round(matriz_I.get_entrada(2,2), 3)) + " "
    + str(round(matriz_I.get_entrada(2,3), 3)))
    print(str(round(matriz_I.get_entrada(3,1), 3)) + " "
    + str(round(matriz_I.get_entrada(3,2), 3)) + " "
    + str(round(matriz_I.get_entrada(3,3), 3)))

