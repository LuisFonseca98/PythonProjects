import numpy as np

def Complemento(b):
    #Calcula o complemento (inverso) de um número binário, caso a diferença de componentes DC seja
    #negativa
    
    c = []
    for num in b:
        if num == '1': 
            c.append('0')
        elif num == '0': 
            c.append('1')
    bit = ''.join(c)
    return bit

def codificadorDC(quant, K):
    tam = quant.shape
    final = []
    coef_DC_anterior = 0
    
    for lin in np.arange(0,tam[0],8): 
        for col in np.arange(0,tam[1],8): 
            bloco = quant[lin:lin+8,col:col+8]
            diferenca = bloco[0][0] - coef_DC_anterior #DC i+1  - DCi
            
            if diferenca < 0:
                #Caso se obtenha um numero negativo, transformamos em binário,
                # e vamos realizar o complemento do numero obtido (contrário)
                bin_neg = bin(int(diferenca))[2:] 
                bin_dif = Complemento(bin_neg)
            else:
                if(diferenca != 0):
                    #Caso a diferenca entre componentes DC seja positiva, transformamos em binário,
                    # e nao é necessário realizar mais nenhuma ação
                    bin_dif = bin(int(diferenca))[2:]
            
            if(bin_dif != None):
                #calcula o numero de bits que sao necessários para representar o numero binario
                #da diferenca entre componentes DC (através de length)
                grandeza = len(bin_dif)
                #consoante o tamanho necessário, vamos obter a codificação respetiva de Huffman
                bin_grandeza = K[grandeza]
                
            if(bin_grandeza != None):
                #finalmente, vamos juntar a codificação de Huffman para os bits necessários para
                # representar a diferença de componentes DC com a própria diferença
                codificado = bin_grandeza + bin_dif
            else:
                #caso a grandeza seja None, é atribuído o valor de Huffman de índice 0 (00)
                codificado = K[0]
            
            #Reiniciamos as variáveis
            bin_dif = None
            bin_grandeza = None
            
            #Colocamos a codificação DC num array
            final.append(codificado)
            #atualizamos o valor do coeficiente anterior, para a próxima iteração
            coef_DC_anterior = bloco[0][0]
    
    final2 = ''.join(final)  
    
    return final2


def descodificadorDC(array,K, altura, largura):
    
    #Cria um array para as componentes DC descodificadas
    final = np.zeros( int( (altura)*(largura) ) )
    
    #inicialização de índice que percorre cada símbolo do array de codificação DC
    posSeg = 0
    #inicialização de índice que serve para colocar os valores descodificados num determinado
    #índice no array "final"
    pos = 0
    
    #Enquanto o índice criado for menor que o array de codificação DC
    while posSeg < len(array):        
        #percorre os items do dicionário, chave atribuída a "grandeza"; valor atribuído a "binario"
        for grandeza,binario in K.items():
            #compara a codificacao de Huffman para os bits necessarios do array com a mesma variável
            # do dicionário
            if array[posSeg:posSeg+len(binario)] == binario:
                #se for igual, então vai buscar a diferença de componentes DC em binário
                #do array
                bit = array[posSeg+len(binario):posSeg+len(binario)+grandeza]
                
                #se a grandez for 0, a diferença entre componentes DC é zero
                if( grandeza == 0):
                    final[pos] = (0)
                
                #se a grandeza não for zero, e o primeiro bit for zero, realizamos o inverso do
                #complemento, passamos para inteiro, e obtemos a diferença de componentes DC
                if( grandeza != 0 and bit[0] == "0"):
                    final[pos] = ((-(int(Complemento(bit),2))))
                
                #se a grandeza não for zero, e o primeiro bit for um, passamos para inteiro,
                #e obtemos a diferença de componentes DC
                if( grandeza != 0 and bit[0] == "1"):
                    final[pos] = ((int(bit,2)))
                
                #atualizamos os indices e saimos do for, e vamos percorrer mais um ciclo de while
                posSeg += len(binario)+grandeza
                pos += 1
                break
    

    #realizamos um reshape do array final
    final = final.reshape(len(final),)
    
    #vamos obter as componentes DC originais, somando o índice atual com o próximo
    for i in range(len(final)-1):
        final[i+1] = final[i]+final[i+1]
        
        
    return final
    