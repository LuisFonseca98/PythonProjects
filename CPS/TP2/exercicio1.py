import numpy as np
p = np.arange(0,10000,1)
nBits = 4

def intTObin(lista,nBits):
    """Converte uma lista de numeros inteiros para binario """
    intToBin = map(lambda x: (np.binary_repr(x,nBits)),lista) #ciclo lambda para percorrer a lista e fazer a representacao dos numeros em binario
    intToBin1 = list(intToBin) #cria uma nova lista da variavel contento lambda
    intToBin2 = ''.join(intToBin1) # junta os indices 
    intToBin3 = ' '.join(intToBin2) #junta os indices
    intToBin4 = intToBin3.split(" ") #separa os indices com aspas
    return np.array(list(intToBin4)).astype(int) #retorna um array, com uma nova lista e com tipo inteiro

def arrayDeCod(lista,nBits):
    """Permite fazer a codificacao do array"""
    copia = lista.copy() #faz uma copia da lista criada na primeira funcao 
    b = len(lista)/4 
    copia.resize(((int)(len(lista)/nBits), nBits))#return uma lista com o tamanho dos bits definidos
    return copia

def binTOint(lista,nBits):
    """Converte uma lista de numeros binarios para numeros inteiros"""
    c = lista.astype(str)  #le o tipo de lista como sendo uma string
    binto = map(lambda x : ''.join(c[x]),range(len(c))) #ciclo lambda, no qual junta os indices da lista, com um range do comprimento de c
    binto1 = list(binto) #cria uma nova lista contendo os indices
    binTOint = map(lambda x: int(binto1[x],2),range(len(binto1))) #ciclo lambda, no qual le os indices do array, com uma incrementacao de 2 em 2
    return np.array(list(binTOint)).astype(int) #return um array, com uma nova lista e do tipo inteiro

