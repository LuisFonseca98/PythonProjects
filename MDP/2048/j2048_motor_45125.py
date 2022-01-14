from random import random
from random import choice

#------------------------------Gerar 0 --------------------------------
def gerar_0(uma_linha):
    nova_linha=[]
    while len(nova_linha) < len(uma_linha):
        nova_linha.append(0)
    return nova_linha

#----------------------------Vitoria---------------------------------
def get_vitoria(grelha):
    resultado = False
    for l in range(len(grelha)):
        for c in range(len(grelha[l])):
            if grelha[l][c] == 2048:
                resultado = True
    return resultado
#------------------------------------------Atualizar_Grelha---------------

def atualizar_grelha(grelha_original, grelha_alterada):
    sao_iguais = True

    for l in range(len(grelha_original)):
        for c in range(len(grelha_original[l])):
            if grelha_original[l][c] != grelha_alterada[l][c]:
                sao_iguais = False

    if not sao_iguais:
        inserir_2ou4(grelha_alterada)

#------------------------------------------ha_iguais_adjacentes---------------
def ha_iguais_adjacentes(grelha):
    ha = False
    # por linhas
    for l in range(len(grelha)):
       for c in range(len(grelha[l]) - 1):
            if (grelha[l][c] != 0) and (grelha[l][c] == grelha[l][c+1]):
                ha = True
    # por colunas
    for l in range(len(grelha) - 1):
        for c in range(len(grelha[l])):
            if(grelha[l][c]!=0) and (grelha[l][c] == grelha[l + 1][c]):
                ha = True
    return ha

#-------------------------------------get_fim------------------------
def get_fim(grelha):
    posicoes_vazias = get_posicoes_vazias(grelha)

    if (len(posicoes_vazias) == 0) and (not ha_iguais_adjacentes(grelha)):

        return True
    else:
        return False



#---------------------ESQUERDA---------------------------------------
def mover_esquerda(uma_linha):
    nova_linha = []
    for valor in uma_linha:
        if valor != 0:
            nova_linha.append(valor)

    while len(nova_linha) < len(uma_linha):
        nova_linha.append(0)

    return nova_linha

def somar_esquerda(uma_linha):
    nova_linha=[]
    pontos = 0
    indice = 0

    while indice < len(uma_linha) - 1:
        if uma_linha[indice] == uma_linha[indice + 1]:
            soma = uma_linha[indice] + uma_linha[indice + 1]
            nova_linha.append(uma_linha[indice] + uma_linha[indice+1])
            pontos = pontos + soma
            indice = indice + 2
        else:
            nova_linha.append(uma_linha[indice])
            indice = indice + 1

    if indice == len(uma_linha) - 1:
        nova_linha.append(uma_linha[indice])

    while len(nova_linha) < len(uma_linha):
        nova_linha.append(0)

    return (nova_linha, pontos)

def esquerda(jogo):
    # jogo é o tuplo:(grelha,fim,vitoria, pontos)

    grelha  = jogo[0]
    fim     = jogo[1]
    vitoria = jogo[2]
    pontos  = jogo[3]
    grelha_alterada = []

    for linha in grelha:
        nova_linha = mover_esquerda(linha)
        (nova_linha2, pontos_somados) = somar_esquerda(nova_linha)
        grelha_alterada.append(nova_linha2)
        pontos = pontos + pontos_somados

    atualizar_grelha(grelha, grelha_alterada)

    fim = get_fim(grelha_alterada)

    if get_vitoria(grelha_alterada) == True:
        vitoria = True

    jogo_alterado = (grelha_alterada, fim, vitoria, pontos)

    return jogo_alterado

#-------------------------------Direita-----------------------------
def reverte_linhas(grelha):

    grelha_revertida = []
    for linha in grelha:
        linha_revertida = []
        l = len(linha)
        for j in range(l):
            linha_revertida.append(linha[l-1-j])
        grelha_revertida.append(linha_revertida)

    return grelha_revertida

def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = reverte_linhas(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_atualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    grelha_revertida = reverte_linhas(grelha)
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_atualizado


#---------------------------- Acima e Abaixo---------------------
def trocar_linhas_com_colunas(grelha):
    resultado = []
    for c in range(len(grelha[0])): # ciclo por colunas
        coluna = []
        for l in range(len(grelha)): # ciclo por linhas
            coluna.append(grelha[l][c])
        resultado.append(coluna) # como sendo uma nova linha

    return resultado

def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado


def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

def valor(jogo, linha, coluna):
    grelha = jogo[0]#tuplo da variavel jogo_alterado(primeiro elemento do array)

    return grelha[linha - 1][coluna - 1]

def terminou(jogo):
    return jogo[1] #tuplo da variavel jogo_alterado(segundo elemento do array)


def ganhou_ou_perdeu(jogo):
    return jogo[2] #tuplo da variavel jogo_alterado(terceiro elemento do array)


def pontuacao(jogo):
    return jogo[3]#tuplo da variavel jogo_alterado(quarto elemento do array)



##-------------Obtêm todas as posiçoes vazias na grelha--------------------------##
def get_posicoes_vazias(grelha):
    posicoes_vazias = []
    for indice_linha in range(4):
        for indice_coluna in range(4):
            if grelha[indice_linha][indice_coluna] == 0:  # Retorna todos os indices onde se encontra um 0
                posicoes_vazias.append([indice_linha, indice_coluna])  # Gera uma lista de todas as posiÃ§Ãµes a 0

    return posicoes_vazias


##---------------------Obtêm uma posição vazia na grelha-------------------##
def get_posicao_vazia(grelha):
    linha = None
    coluna = None

    posicoes_vazias = get_posicoes_vazias(grelha)

    for indice_linha in range(4):
        for indice_coluna in range(4):
            if grelha[indice_linha][indice_coluna] == 0:  # Retorna todos os indices onde se encontra um 0
                posicoes_vazias.append([indice_linha, indice_coluna])  # Gera uma lista de todas as posiÃ§Ãµes a 0

    posicao_vazia = choice(posicoes_vazias)  # Escolhe 1 das posiÃ§Ãµes a 0

    linha = posicao_vazia[0]
    coluna = posicao_vazia[1]

    return [linha, coluna]


##--------------------------função que obtem um 2 ou um 4------------------------##

def get_2ou4():
    x= random()
    if x > 0.1:
        return 2
    else:
        return 4


##-----------------------Insere um 2 ou um 4 na grelha-------------------##
def inserir_2ou4(grelha):
    dois_ou_quatro = get_2ou4()
    posicoes_vazias = get_posicoes_vazias(grelha)
    posicao_vazia = choice(posicoes_vazias)
    indice_linha = posicao_vazia[0]
    indice_coluna = posicao_vazia[1]
    grelha[indice_linha][indice_coluna] = dois_ou_quatro


##-----------------------NOVO JOGO------------------------------##
def novo_jogo():  # re-inicializar variaveis do jogo

    grelha = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    fim = False
    vitoria = False
    pontos = 0

    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
    jogo = (grelha, fim, vitoria, pontos)

    return jogo
