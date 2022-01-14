import cv2
import matplotlib.pyplot as plt
import numpy as np

baseDados = "database/"
#file = "P1000697s.jpg"
#file = "P1000698s.jpg"
#file = "P1000699s.jpg"
#file = "P1000703s.jpg"
#file = "P1000705s.jpg"
#file = "P1000706s.jpg"
#file = "P1000709s.jpg"
#file = "P1000710s.jpg"
file = "P1000713s.jpg"

img = cv2.imread(baseDados + file)
#cv2.imshow("Imagem Original", img)

"""Transforma a imagem original em tons de cinzento"""
def grayImg(img):
    grey = img[:,:,2] #retira a componente azul, que esta em mais abundancia
    #print("grey",grey)
    pb = cv2.add(grey, np.array([120.0]))
    #cv2.imshow('Imagem de teste',grey)
    #print("pb",pb)
    return pb

"""Transforma a imagem em preto e branco"""
def threshold(grayImg):
    img,binario = cv2.threshold(grayImg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow('Imagem Binaria',binario)
    return binario

"""Calcula o histograma"""
def histograma(img):
    hist = cv2.calcHist(img, [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()

"""Melhoramento da imagem quando passa pela binarização"""
def melhoramento(binImg):
    imgBlur = cv2.medianBlur(binImg,5)
    kernell = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7),(-1,-1))
    
    morfologia = cv2.morphologyEx(imgBlur,cv2.MORPH_CLOSE,kernell) #permite remover "ruido" no background da imagem
    erosao = cv2.erode(imgBlur,kernell,iterations = 14) #permite tirar contorno a objetos
    dilate = cv2.dilate(erosao,kernell,iterations = 10) #permite adicionar contorno a objetos
    #cv2.imshow("Imagem Melhorada",dilate)
    return dilate

"""Permite extrair os componentes existentes numa imagem, quando melhoramos a imagem"""
def extrairComponentes(imgMelhorada):
    #hieraruia: se os objetos estao uns em cima dos outros
    contours,Hierarchy = cv2.findContours(imgMelhorada, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours


"""Metodo que retorna moedas numa imagem"""
def extrairMoedas(componentes):
    moedas = []
    for i in range(len(componentes)):
        if 12 < circularidade(componentes,i) < 14:
            moedas.append(componentes[i])
    return moedas

"""Metodo que deteta quais os objetos na imagem tem uma figura circular"""
def circularidade(componentes,i):
    numerador = cv2.arcLength(componentes[i], False) ** 2 # calcula o perimetro
    denominador = cv2.contourArea(componentes[i]) #calcula a area de um circulo
    circularidade = numerador/denominador
    return circularidade

"""Método que classifica as diferentes moedas"""
def classificaMoeda(moedas):
    valor = np.zeros(len(moedas))
    for i in range(len(moedas)):
        area = cv2.contourArea(moedas[i])
        if 6100 < area < 6500:
            valor[i] = 0.01
        elif 9200 < area < 9600:
            valor[i] = 0.02
        elif 10100 < area < 10900:
            valor[i] = 0.10
        elif 11500 < area < 12500:
            valor[i] = 0.05
        elif 13300 < area < 14400:
            valor[i] = 0.2
        elif 15200 < area < 16000:
            valor[i] = 1
        elif 16800 < area < 17500:
            valor[i] = 0.5
        elif 18500 < area < 20500:
            valor[i] = 2
        else:
            valor[i] = 0
        #print(i,"",area)
    return valor

"""Mete um titulo, distinguindo as diferentes moedas que existem nas imagens"""
def colocarTituloRespetivaMoeda(img,moedas,valor):
    cor = (0,0,255)
    tamanhoFonte = 4
    larguraTexto = 3
    
    for i in range(len(moedas)):
        pos = (moedas[i][0][0][0],moedas[i][0][0][1])
        valorMoedas = str(valor[i])
        cv2.putText(img, valorMoedas, pos, cv2.FONT_HERSHEY_PLAIN, tamanhoFonte, cor, larguraTexto)
        #cv2.putText(img, str(i), pos, cv2.FONT_HERSHEY_PLAIN, tamanhoFonte, cor, larguraTexto)
        #print(i,"",valorMoedas,""," valor ")
    return img
        

"""Calcula o valor total das moedas, colocando uma legenda com o seu respetivo valor total"""
def calcularValorTotal(img,valor):
    valorTotal = np.round(np.sum(valor),3)
    pos = (100,650)
    cor = (0,0,0)
    tamanhoFonte = 4
    larguraTexto = 3
    textValor = "Total: " + str(valorTotal) + " Euros"
    #cv2.putText(imagem,posicaoTexto,fonte,tamanhoFonte,corTexto,larguraTexto)
    cv2.putText(img,textValor,pos,cv2.FONT_HERSHEY_PLAIN,tamanhoFonte,cor,larguraTexto)
    return img


imgBW = grayImg(img)
#histograma(imgBW)
binImg = threshold(imgBW)
melhoramentoImg = melhoramento(binImg)
extracaoComp = extrairComponentes(melhoramentoImg)
moedas = extrairMoedas(extracaoComp)

classificacao = classificaMoeda(moedas)
etiquetarMoedas = colocarTituloRespetivaMoeda(img,moedas,classificacao)
valorTotal = calcularValorTotal(img,classificacao)

cv2.imshow('Resultado Final',valorTotal)

cv2.waitKey(0)
cv2.destroyAllWindows()
