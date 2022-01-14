#funcoes motor
from jogo_2048_motor_A45125 import novo_jogo
from jogo_2048_motor_A45125 import valor
from jogo_2048_motor_A45125 import terminou
from jogo_2048_motor_A45125 import pontuacao
from jogo_2048_motor_A45125 import esquerda
from jogo_2048_motor_A45125 import direita
from jogo_2048_motor_A45125 import acima
from jogo_2048_motor_A45125 import abaixo

#funcoes gestor
from jogo_2048_gestor_A45125 import  le_identificacao
from jogo_2048_gestor_A45125 import  inicializa_semente
from jogo_2048_gestor_A45125 import  regista_jogada
from jogo_2048_gestor_A45125 import  regista_grelha_inicial
from jogo_2048_gestor_A45125 import  regista_pontos
from jogo_2048_gestor_A45125 import  escreve_registo
from jogo_2048_gestor_A45125 import  regista_ranking                    

def alinhar(uma_string):
    return uma_string

def print_2048(jogo):
    pontos = pontuacao(jogo)

    print("pontos =" + str(pontos))

    for l in range(4):
        linha_string = ""
        for c in range(4):
            linha_string = linha_string + alinhar(str(valor(jogo, l + 1, c + 1))) + " "
        print(linha_string)

le_identificacao()
inicializa_semente(None)
jogo = novo_jogo()
print_2048(jogo)

regista_grelha_inicial(
    valor(jogo, 1,1), valor(jogo, 1,2), valor(jogo, 1,3), valor(jogo, 1,4),
    valor(jogo, 2,1), valor(jogo, 2,2), valor(jogo, 2,3), valor(jogo, 2,4),
    valor(jogo, 3,1), valor(jogo, 3,2), valor(jogo, 3,3), valor(jogo, 3,4),
    valor(jogo, 4,1), valor(jogo, 4,2), valor(jogo, 4,3), valor(jogo, 4,4))

print("Pressione n para comecar um novo jogo")
print("Pressione q para sair do jogo")

tecla = None
while tecla != 'q' and not (terminou(jogo)):

    tecla = input()

    if tecla == 'n':
        jogo = novo_jogo()

    elif tecla == 'a':
        jogo = esquerda(jogo)
        regista_jogada(tecla)

    elif tecla == 's':
        jogo = abaixo(jogo)
        regista_jogada(tecla)

    elif tecla == 'd':
        jogo = direita(jogo)
        regista_jogada(tecla)

    elif tecla == 'w':
        jogo = acima(jogo)
        regista_jogada(tecla)


    print_2048(jogo)

regista_pontos(pontuacao(jogo))
mensagem_cloud=escreve_registo()
print("Game Over")
print(mensagem_cloud)
