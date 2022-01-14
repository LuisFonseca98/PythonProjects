
def novo_jogo():
    grelha = [[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]
   
    fim = False
    vencedor = None
    jogador = 1
    linha_vitoria = None
    jogo = (grelha,fim,vencedor,jogador,linha_vitoria)
    
    return jogo

def ha_espaco(jogo, coluna):
    grelha = jogo[0]
    for indice_linha in range(6):
        if grelha[indice_linha][coluna-1] == 0:
            return True
    return False    

def jogar(jogo, coluna):
    grelha = jogo[0]
    fim = jogo[1]
    vencedor = jogo[2]
    jogador = jogo[3]
    linha_vitoria = jogo[4]

    #verifica se há espaço para jogar
    if ha_espaco(jogo, coluna):
        for in_linha in reversed(range(6)):
            if grelha[in_linha][coluna-1] == 0:
                grelha[in_linha][coluna-1] = jogador
                break

        #verifica na horizontal ( - ) se alguém ganhou
        for in_linha in range(6):
            for in_coluna in range(4):
                if grelha[in_linha][in_coluna] == grelha[in_linha][in_coluna+1] == grelha[in_linha][in_coluna+2] == grelha[in_linha][in_coluna+3] == jogador:
                    fim = True
                    vencedor = jogador
                    linha_vitoria = [[in_linha+1,in_coluna+1],[in_linha+1,in_coluna+2],[in_linha+1,in_coluna+3],[in_linha+1,in_coluna+4]]

        #verifica na vertical ( | ) se alguém ganhou
        for in_linha in range(3):
            for in_coluna in range(7):
                if grelha[in_linha][in_coluna] == grelha[in_linha+1][in_coluna] == grelha[in_linha+2][in_coluna] == grelha[in_linha+3][in_coluna] == jogador:
                    fim = True
                    vencedor = jogador
                    linha_vitoria = [[in_linha+1,in_coluna+1],[in_linha+2,in_coluna+1],[in_linha+3,in_coluna+1],[in_linha+4,in_coluna+1]]

        #verifica na diagonal ( \ ) se alguém ganhou
        for in_linha in range(3):
            for in_coluna in range(4):
                if grelha[in_linha][in_coluna] == grelha[in_linha+1][in_coluna+1] == grelha[in_linha+2][in_coluna+2] == grelha[in_linha+3][in_coluna+3] == jogador:
                    fim = True
                    vencedor = jogador
                    linha_vitoria = [[in_linha+1,in_coluna+1],[in_linha+2,in_coluna+2],[in_linha+3,in_coluna+3],[in_linha+4,in_coluna+4]]

        #verifica na diagonal ( / ) se alguém ganhou
        for in_linha in range(4,6):
            for in_coluna in range(4):
                if grelha[in_linha][in_coluna] == grelha[in_linha-1][in_coluna+1] == grelha[in_linha-2][in_coluna+2] == grelha[in_linha-3][in_coluna+3] == jogador:
                    fim = True
                    vencedor = jogador
                    linha_vitoria = [[in_linha+1,in_coluna+1],[in_linha,in_coluna+2],[in_linha-1,in_coluna+3],[in_linha-2,in_coluna+4]]


        #caso para o empate
        i=0
        for in_linha in range(6):
            for in_coluna in range(7):
                if grelha[in_linha][in_coluna]!= 0:
                    i=i+1
        if i==42:
            fim=True

        #atualização para o próximo jogador
        if (jogador%2)==0:
            jogador=1
        else:
            jogador=2

    #caso já não haja espaços para jogar
    else:
        #caso para o empate
        i=0
        for in_linha in range(6):
            for in_coluna in range(7):
                if grelha[in_linha][in_coluna]!=0:
                    i=i+1
        if i==42:
            fim=True

    novojogo = (grelha, fim, vencedor, jogador, linha_vitoria)
    return novojogo
       
       
def valor(jogo,linha,coluna):
    grelha = jogo[0]
    return grelha[linha-1][coluna-1]

def terminou(jogo):
    terminou = jogo[1]
    return terminou

def quem_ganhou(jogo):
    vitoria = jogo[2]
    return vitoria

def get_linha_vitoria(jogo): 
    linhaVitoria = jogo[4]
    return linhaVitoria
