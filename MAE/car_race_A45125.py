#-*- coding: utf-8 -*-
#Quem usar Python2 precisa de incluir isto... no Python3 não...  
#(tem a ver com a codificação do texto)
# O intrepretador de Python 2 assume que o programa está escrito em
# ASCII. Como em ASCII não existem os carateres acentuados do
# português todos os comentários escritos em português dão erro
# (caracter inválido). A forma de contornar isto em Python 2 é indicar
# que o programa está escrito em utf8 (é uma norma de codificação de
# caracteres Unicode. Os caracteres Unicode têm comprimento ilimitado
# e por isso acomodam totas as línguas presentes e futuras :-)). O
# intrepretador Python 3 já assume que o programa está escrito em
# Unicode/utf8 e por isso não é preciso fazer nada.


# Importar o módulo pygame
# se a execução deste import em Python3 ou Python2 der algum erro
# é porque o pygame não está bem instalado
import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt, pi


# inicialização do módulo pygame
pygame.init()


#musica de fundo

pygame.mixer.music.load("Metroid Prime 3 Corruption Music.wav")
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play(-1)

# criação de uma janela
largura = 500
altura  = 500
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Car_Race_A45125') #nome da janela
#Nesta janela o ponto (0,0) é o canto superior esquerdo
#e (532-1,410-1) = (531,409) o canto inferior direito.

# número de imagens por segundo
frame_rate = 20

# relógio para controlo do frame rate
clock = pygame.time.Clock()

# ler uma imagem em formato bmp
pista = pygame.image.load("car_track.png")
carro = pygame.image.load("metroid_morph_ball.png")
#Inicializa o tempo
t=0.0


#########################
#Para escrever o tempo:
font_size = 20
font = pygame.font.Font(None, font_size) # fonte pré-definida
antialias = True # suavização
WHITE = (255, 255, 255)# cor (terno com os valores Red, Green, Blue entre 0 e 255)
#######################

#(A) Se descomentar aqui (e comentar B) vejo onde passou/ rasto da trajetória
# Pois neste caso só junta a pista uma vez,
#no outro caso está sempre a juntar/desenhar a pista
##janela.blit(pista, (0, 0)) 

def fim_do_jogo(text,font):
    textSurface = font.render(text,True,(255,128,0))
    return textSurface, textSurface.get_rect()

##################################
##Exemplo ajustado à pista

def parametrizacao (t):
    if t==0:
        resultado=(110,45)
    if 0<t<=3:
        resultado=(110+110*t,45) 
    if 3<t<=4.40:
        resultado=(435+5*cos((t-3)*(pi/2)+3*pi/2),45+50*sin(t-3))
    if 4.40<t<=5.3:
        resultado=(440,94+344*(t-4.4))
    if 5.3<t<=5.4:
        resultado=(415+24*cos(t-5.3),450-34*sin(t-5.3))
    if 5.4<t<=5.9:
        resultado=(420-200*(t-5.4),445)
    if 5.9<t<=6.4:
        resultado=(320,458 -420*(t-5.9))
    if 6.4<t<=9.9:
        resultado=(265-55*cos(t-3.5),190+50*sin(t-3.5))
    if 9.9<t<=11:
        resultado=(212,221+180*(t-9.9))
    if 11<t<=12.0:
        resultado=(212-165*sin(t-11),390+50*cos(t-11))
    if 12.0<t<=12.9:
        resultado=(70,400-335*(t-12.0))
    if 12.9<t<=13.1:
        resultado=(75-80*sin(-t+12.9),90-45.2*cos(-t+12.9))
    if t>=13.1:
        resultado=(110,45)
        largeText=pygame.font.SysFont("comicsansms",60)
        smallText=pygame.font.SysFont("comicsansms",20)
        TextSurf,TextRect = fim_do_jogo("Game Over",largeText)
        TextSurf1,TextRect1 = fim_do_jogo("Press r to start a new game",smallText)
        TextRect.center=((largura/2),(altura/2))
        TextRect1.center=((largura/2),(altura/1.7))
        janela.blit(TextSurf,TextRect)
        janela.blit(TextSurf1,TextRect1)
    return resultado


#################################
#Ciclo principal do jogo

while True:
    if 0<t<13.1:
        carro=pygame.transform.rotate(carro,-90)
        
    tempo = font.render("t="+str(t), antialias, WHITE)
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    janela.blit(carro, parametrizacao(t))
    janela.blit(tempo, (10, 10))
    pygame.display.update()
    clock.tick(frame_rate)
    t=t+0.1
        

    for event in pygame.event.get():
        #Para sair...
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Ao clicar em qualquer local, o tempo recomeça com t=0
        # evento mouse click botão esquerdo (código = r)
        elif event.type== pygame.KEYDOWN:
            if event.key==pygame.K_r:
                t = 0
                       

##        #Quando queremos saber as coordenadas de um ponto: 
##        # descomentar isto e comentar o "evento mouse click"...
##        #"clicar" nesse ponto... o python print as coordenadas.
##        # evento mouse click botão esquerdo (código = 1)
##        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
##            (x, y) = event.pos
##            localizacao="posicao=(" + str(x) + "," + str(y) + ")"
##            print(localizacao)


##FAQs:
##            (1)
##            Quando parametrização (ou velocidade) não está definida
##           para algum valor de t, dá o erro:
##                "local variable "result/resultado" referenced before assignment"
##            
            




