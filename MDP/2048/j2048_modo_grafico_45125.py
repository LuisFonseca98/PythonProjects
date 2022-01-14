import pygame
import os
import sys
from pygame.locals import *
from random import randint 
#----------------------------MOTOR---------------------------
from j2048_motor_45125 import novo_jogo
from j2048_motor_45125 import valor
from j2048_motor_45125 import terminou
from j2048_motor_45125 import pontuacao
from j2048_motor_45125 import esquerda
from j2048_motor_45125 import direita
from j2048_motor_45125 import acima
from j2048_motor_45125 import abaixo
from j2048_motor_45125 import ganhou_ou_perdeu
#----------------------------GESTOR--------------------------
from j2048_gestor_45125 import  le_identificacao
from j2048_gestor_45125 import  inicializa_semente 
from j2048_gestor_45125 import  regista_jogada
from j2048_gestor_45125 import  regista_grelha_inicial
from j2048_gestor_45125 import  regista_pontos
from j2048_gestor_45125 import  escreve_registo
from j2048_gestor_45125 import  regista_ranking          

#variaveis globais
x = 140
y = 100
grelha_x = 40
grelha_y = 40
grelha_posicao = (grelha_x, grelha_y)
grelha_linha = 15
grelha_margem= 50
grelha_quadrados = 100
grelha_tamanho = (300, 300)
screen_tamanho = (1000,640)
restart_tamanho=(72,125)

estado = {'menu':0,'jogavel':1,'gameover':2,'vitoria':3, 'depois_da_vitoria':4} #dicionario com estados
estado_jogo = 0 #estado do automato jogo
count_frame = 0 #para a contagem de tempo
estado_som = 0 #para controlar efeitos sonoros
estado_som_2 = 0 #segunda variavel para controlar os efeitos sonoros
frame_rate = 60


#variaveis para as fotos e sons
background = pygame.transform.scale(pygame.image.load("Imagens/metroid_retro2.PNG"), screen_tamanho)
imagem_botao_nao_pressionado = pygame.transform.scale(pygame.image.load("Imagens/start_menu.PNG"), screen_tamanho)
imagem_botao_pressionado = pygame.transform.scale(pygame.image.load("Imagens/start_menu_2.PNG"), screen_tamanho)
Imagem_2 = pygame.transform.scale(pygame.image.load("Imagens/2.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_4 = pygame.transform.scale(pygame.image.load("Imagens/4.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_8 = pygame.transform.scale(pygame.image.load("Imagens/8.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_16 = pygame.transform.scale(pygame.image.load("Imagens/16.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_32 = pygame.transform.scale(pygame.image.load("Imagens/32.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_64 = pygame.transform.scale(pygame.image.load("Imagens/64.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_128= pygame.transform.scale(pygame.image.load("Imagens/128.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_256 = pygame.transform.scale(pygame.image.load("Imagens/256.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_512 = pygame.transform.scale(pygame.image.load("Imagens/512.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_1024 = pygame.transform.scale(pygame.image.load("Imagens/1024.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_2048 = pygame.transform.scale(pygame.image.load("Imagens/2048.PNG"), (grelha_quadrados, grelha_quadrados))
Imagem_vitoria_1=pygame.transform.scale(pygame.image.load("Imagens/Metroid_2048_Victory_1.PNG"),screen_tamanho)
Imagem_vitoria_2=pygame.transform.scale(pygame.image.load("Imagens/Metroid_2048_Victory_2.PNG"),screen_tamanho)
Restart = pygame.transform.scale(pygame.image.load("Imagens/restart1.PNG"),restart_tamanho)
Imagem_gameover_1 = pygame.transform.scale(pygame.image.load("Imagens/game_over3.PNG"), screen_tamanho)
Imagem_gameover_2 = pygame.transform.scale(pygame.image.load("Imagens/game_over_4.PNG"), screen_tamanho)
Imagem_gameover_3 = pygame.transform.scale(pygame.image.load("Imagens/game_over5.PNG"),screen_tamanho)

#variaveis para os efeitos sonoros
pygame.mixer.init()
move_sound = pygame.mixer.Sound("sound/metroid_move_sound.WAV")
sound_metroid = pygame.mixer.Sound("sound/metroid_sound.WAV")
sound_buttom = pygame.mixer.Sound("sound/metroid_sound_buttom.WAV")

#inicia a font
pygame.font.init()
largeText = pygame.font.Font("VoiceActivatedBB_ital.ttf", 70)
t = pygame.font.Font("VoiceActivatedBB_ital.ttf", 25)

#-----------------------FUNCOES------------------------------------

#coloca no lugar de numeros na grelha, as imagens correspondentes
def grelha_quadrado(jogo, linha, coluna, screen):
    d = valor(jogo, linha, coluna)
    if d== 0:
        return grelha_quadrado
    if d == 2:
        screen.blit(Imagem_2, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha))) # posicao x = 35 do tabuleiro, largura da linha = 19, quadrado = 135
    elif d == 4:
        screen.blit(Imagem_4, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha))) # Ajustar esses valores de acordo com o vosso tabuleiro
    elif d == 8:
        screen.blit(Imagem_8, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 16:
        screen.blit(Imagem_16, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 32:
        screen.blit(Imagem_32, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 64:
        screen.blit(Imagem_64, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 128:
        screen.blit(Imagem_128, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 256:
        screen.blit(Imagem_256, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 512:
        screen.blit(Imagem_512, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 1024:
        screen.blit(Imagem_1024, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
    elif d == 2048:
        screen.blit(Imagem_2048, (grelha_x + grelha_margem + (coluna - 1) * (grelha_quadrados + grelha_linha), grelha_y + grelha_margem + (linha - 1) * (grelha_quadrados + grelha_linha)))
        
#inicializa um novo jogo e guarda os pontos para o ranking
def new_game(jogo):
    regista_pontos(pontuacao(jogo))
    mensagem_cloud = escreve_registo()
    print(mensagem_cloud)
    le_identificacao()
    inicializa_semente(None)

    jogo = novo_jogo()

    regista_grelha_inicial(valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3), valor(jogo, 1, 4),
                           valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3), valor(jogo, 2, 4),
                           valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3), valor(jogo, 3, 4),
                           valor(jogo, 4, 1), valor(jogo, 4, 2), valor(jogo, 4, 3), valor(jogo, 4, 4))
    return jogo

#coloca a grelha e imagens dos numeros no ecrã
def mostrar_grelha (jogo, screen):
    screen.blit(background, (0,0))  
    for linha in range(4):
        for coluna in range(4):
            grelha_quadrado(jogo, linha+1, coluna+1, screen)

#coloca a imagem de vitoria no ecrã
def victory_screen():
    screen.blit(Imagem_vitoria_1, (0,0))

#retorno ao estado jogavel
def retorna_estado():
    mostrar_grelha(jogo, screen)
    p = largeText.render("Pontos:", True, (255, 255, 255))  # cor do texto, cor da screen
    screen.blit(p, (600, 200))

    P = largeText.render(str(pontuacao(jogo)), True, (255, 255, 255))  # cor do texto, cor da screen
    screen.blit(P, (600, 260))
#----------------------------------------------------------PARTE GRAFICA------------------------------
# inicia pygame            
pygame.init()
screen = pygame.display.set_mode((screen_tamanho))
pygame.display.set_caption("JOGO 2048")
clock = pygame.time.Clock()

#musica de fundo
pygame.mixer.music.load("sound/Metroid Samus Returns.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

# funcao motor
le_identificacao()
inicializa_semente(None)
jogo = novo_jogo()
regista_grelha_inicial(valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3), valor(jogo, 1, 4),
                       valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3), valor(jogo, 2, 4),
                       valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3), valor(jogo, 3, 4),
                       valor(jogo, 4, 1), valor(jogo, 4, 2), valor(jogo, 4, 3), valor(jogo, 4, 4))

fim = False
while fim == False:

    #controlo dos key_presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True

        elif event.type == pygame.KEYDOWN and (estado_jogo==estado['jogavel'] or estado_jogo==estado['depois_da_vitoria']):
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                jogo = esquerda(jogo)
                regista_jogada('- left - ')
                move_sound.play()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                jogo = abaixo(jogo)
                regista_jogada('- down -')
                move_sound.play()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                jogo = direita(jogo)
                regista_jogada('- right - ')
                move_sound.play()
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                jogo = acima(jogo)
                regista_jogada('- up -')
                move_sound.play()
#-----------------------------------------------------------Estados e Butoes--------------------------------
    #menu inicial
    if estado_jogo == estado['menu']:
        count_frame=count_frame + 1
        screen.blit(imagem_botao_nao_pressionado,(0,0))
        B = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if count_frame >5:
           if 320>mouse[0]>100 and 450>mouse[1]>350:
                screen.blit(imagem_botao_pressionado, (0, 0))
                if estado_som==0:
                    sound_buttom.play()
                    estado_som=1
                if B[0]:
                    estado_jogo = 1
           else:
               estado_som=0


    #estado jogavel
    elif estado_jogo == estado['jogavel']:
         retorna_estado()
         mouse = pygame.mouse.get_pos()
         B = pygame.mouse.get_pressed()
         if 670 > mouse[0] > 590 and 450 > mouse[1] > 410:   
            screen.blit(Restart, (590, 360))
            if estado_som==0:
                sound_buttom.play()
                estado_som=1
         else:
            estado_som=0
         if B[0] and 650 > mouse[0] > 555 and 450 > mouse[1] > 410:
            print(pontuacao(jogo))
            jogo = new_game(jogo)
         if terminou(jogo):
            estado_jogo = 2
         if ganhou_ou_perdeu(jogo):
            estado_jogo = 3
    #estado game over
    elif estado_jogo == estado['gameover']:
        pygame.mixer.music.play(-1)
        screen.blit(Imagem_gameover_1,(0,0))
        B = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 850>mouse[0]>150 and 480>mouse[1]>395:  
                screen.blit(Imagem_gameover_2, (0,0))
                if B[0]:
                    print(pontuacao(jogo))
                    jogo = new_game(jogo)
                    estado_jogo=1
                if estado_som==0:
                    sound_buttom.play()
                    estado_som=1
        elif 780>mouse[0]>150 and 570>mouse[1]>500:
                screen.blit(Imagem_gameover_3, (0,0))
                if B[0]:
                    print(pontuacao(jogo))
                    jogo = new_game(jogo)
                    estado_jogo=0
                if estado_som==0:
                    sound_buttom.play()
                    estado_som=1
        else:
            estado_som=0
                
    #estado vitoria
    elif estado_jogo == estado['vitoria']:
        pygame.mixer.music.play(-1)
        victory_screen()
        B = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 850 > mouse[0] > 650 and 550 > mouse[1] > 300:
            screen.blit(Imagem_vitoria_2,(0,0))
            if B[0] and 850 > mouse[0] > 650 and 550 > mouse[1] > 300:
                estado_jogo = 4
            if estado_som==0:
                sound_metroid.play()
                estado_som=1
        else:
            screen.blit(Imagem_vitoria_1,(0,0))
            estado_som=0

##    #estado jogavel ao chegar ao objectivo (já não testa se ganhou)
    elif estado_jogo == estado['depois_da_vitoria']:
         retorna_estado()
         pygame.mixer.music.set_volume(1)
         mouse = pygame.mouse.get_pos()
         B = pygame.mouse.get_pressed()
         if 650 > mouse[0] > 555 and 450 > mouse[1] > 410:
            screen.blit(Restart, (590, 360))
            if estado_som==0:
                sound_buttom.play()
                estado_som=1

            if B[0] and 650 > mouse[0] > 555 and 450 > mouse[1] > 410:
                print(pontuacao(jogo))
                jogo = new_game(jogo)
         else:
            estado_som=0
            if terminou(jogo):
                estado_jogo = 2

    clock.tick(frame_rate)

    pygame.display.flip()

print(pontuacao(jogo))
regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()
print(mensagem_cloud)
pygame.quit()
