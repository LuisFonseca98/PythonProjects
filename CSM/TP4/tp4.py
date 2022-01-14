import cv2
import numpy as np
from time import time
import matplotlib.pyplot as plt
import os
import sys


N = 11
n = range(N)
img_original_names = []
img_ball = []
for k in n:
    image_in = "seq_bola_bmp/bola_%02d.bmp" % k
    img_original_names.append(image_in)
    x = cv2.imread(image_in, cv2.IMREAD_GRAYSCALE)
    img_ball.append(x)
    

def measure_CompressionRatio(img_orig, img_comp):
    size_ImgOrig = os.path.getsize(img_orig)
    size_ImgComp = os.path.getsize(img_comp) 
    return size_ImgOrig / size_ImgComp 

def measure_Entropy(x):
    Max= 255 # for the uint8 datatype
    prob, dummy = np.histogram(x.ravel(),np.arange(0,Max),density=True)
    return -sum(prob*np.log2(prob+sys.float_info.min))


def measure_SNR(img_orig, img_final):
    Dim = np.prod(img_orig.shape)
    img_b = img_orig.astype(np.float64)
    img_e = img_final.astype(np.float64)
    pot_img = np.sum( img_b ** 2 )/Dim
    pot_err = np.sum((img_b - img_e)**2)/Dim 
    SNR = 10 * np.log10( pot_img / pot_err )
    return SNR

def measure_Energy(imagem):
    img = cv2.imread(imagem, cv2.IMREAD_COLOR)
    altura = img.shape[0]
    largura = img.shape[1]
    r, g, b = cv2.split(img)
    sR = [[int(elem) * int(elem) for elem in inner] for inner in r]
    sG = [[int(elem) * int(elem) for elem in inner] for inner in g]
    sB = [[int(elem) * int(elem) for elem in inner] for inner in b]
    energy = (np.sum(sR) + np.sum(sG) + np.sum(sB))*1.0 / (largura * altura)
    return energy*1.0


def MAE(bloco1,bloco2):    
    return np.sum(abs((1.0 * bloco1) - (1.0 * bloco2)))


def mostrar_graficos(snr, tc, entropia, energia, mostrar = None):
    if mostrar =="snr":
        plt.plot(snr)
        plt.title("SNR")
        plt.xlabel("numero imagem",fontsize = 10)
        plt.ylabel("snr da imagem",fontsize = 10)
        plt.grid()
        plt.show()
        
    elif mostrar == "tc":
        plt.plot(tc)
        plt.title("TC")
        plt.xlabel("numero imagem",fontsize = 10)
        plt.ylabel("tc da imagem",fontsize = 10)
        plt.grid()
        plt.show()
    elif mostrar == "entropia":
        plt.plot(entropia)
        plt.title("ENTROPIA")
        plt.xlabel("numero imagem",fontsize = 10)
        plt.ylabel("entropia da imagem",fontsize = 10)
        plt.grid()
        plt.show()
    elif mostrar == "energia":
        plt.plot(energia)
        plt.title("ENERGIA")
        plt.xlabel("numero imagem",fontsize = 10)
        plt.ylabel("energia da imagem",fontsize = 10)
        plt.grid()
        plt.show()
    else:
        mostrar_graficos(snr, tc, entropia, energia, "snr")
        mostrar_graficos(snr, tc, entropia, energia, "tc")
        mostrar_graficos(snr, tc, entropia, energia, "entropia")
        mostrar_graficos(snr, tc, entropia, energia, "energia")


def codificadorIntraFrame(imagens, qualidade):
    snr = []
    tc = []
    entropia = []
    energia = []
    jpg_ball = []
    
    for i in range(len(imagens)):
        cv2.imwrite("IntraFrame/bola_%02d.jpg"%i, imagens[i], (cv2.IMWRITE_JPEG_QUALITY, qualidade))
        img_jpg = cv2.imread("IntraFrame/bola_%02d.jpg"%i, cv2.IMREAD_GRAYSCALE)
        jpg_ball.append(img_jpg)
        snr.append(measure_SNR(imagens[i], img_jpg))
        tc.append(measure_CompressionRatio(img_original_names[i], "IntraFrame/bola_%02d.jpg"%i))
        entropia.append(measure_Entropy(img_jpg))
        energia.append(measure_Energy("IntraFrame/bola_%02d.jpg"%i))
                
    return jpg_ball, snr, tc, entropia, energia

t1 = time()
qualidade = 50
jpg_ball,snr_ball,tc_ball,entropia_ball,energia_ball = codificadorIntraFrame(img_ball, qualidade)
t2 = time()
print("Tempo da codificação Intra-Frame: " + str(t2-t1))




def codificadorInterFrame(imagens, qualidade):
    coded_img = []
    snr = []
    tc = []
    entropia = []
    energia = []

    Iframe = cv2.imread(img_original_names[0], cv2.IMREAD_GRAYSCALE)
    coded_img.append(Iframe)
    cv2.imwrite("InterFrame_codificacao/bola_coded_00.jpg", Iframe, (cv2.IMWRITE_JPEG_QUALITY, qualidade))


    for i in range(1, len(imagens)):
        imagem_lida = cv2.imread(img_original_names[i], cv2.IMREAD_GRAYSCALE)
        imagem_lida = imagem_lida.astype(float)
        Pframe = (imagem_lida - Iframe)
        coded_img.append(Pframe)
        cv2.imwrite("InterFrame_codificacao/bola_coded_%02d.jpg"%i,Pframe,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        snr.append(measure_SNR(imagens[i], Pframe))
        tc.append(measure_CompressionRatio(img_original_names[i], "InterFrame_codificacao/bola_coded_%02d.jpg"%i))
        entropia.append(measure_Entropy(Pframe))
        energia.append(measure_Energy("InterFrame_codificacao/bola_coded_%02d.jpg"%i))
        
        
    return coded_img, snr, tc, entropia, energia

t0 = time()        
coded_ball,snr_ball,tc_ball,entropia_ball, energia_ball = codificadorInterFrame(img_ball, qualidade)  
t1 =time()
print("Tempo da codificação Inter-Frame: "+str(t1-t0))


mostrar_graficos(snr_ball, tc_ball, entropia_ball, energia_ball)

def descodificadorInterFrame(imagens_originais, imagens_codificadas, qualidade):
    decoded_img = []
    x_img = imagens_originais[0].astype('float64')
    for i in range(1, len(imagens_originais)):
        new_img = x_img.copy()
        dif = imagens_codificadas[i].astype('float64')
        dif +=  new_img
        decoded_img.append(dif)
        cv2.imwrite("InterFrame_descodificacao/bola_decoded_%02d.jpg"%i,dif,(cv2.IMWRITE_JPEG_QUALITY, qualidade))
    return decoded_img

t0 = time()
decoded_ball = descodificadorInterFrame(img_ball, coded_ball, qualidade)
t1 = time()
print("Tempo da descodificação Inter-Frame: " + str(t1-t0))


def codificacaoCompensacaoMovimento(imagens, qualidade):
    i_frame = cv2.imread(img_original_names[0], cv2.IMREAD_GRAYSCALE)
    
    cv2.imwrite( "InterFrame_compensacao_codificacao/seq3_bola_00.jpg", i_frame, (cv2.IMWRITE_JPEG_QUALITY,qualidade))
    
    altura, largura = i_frame.shape
    index = 0
    vetor = np.zeros(int  (  (((altura*largura)/(16*16)) *2)*len(imagens)  )  )
    vetor = vetor.reshape( int ((altura*largura)/(16*16)), len(imagens)*2)
    
    for img in range(1, len(imagens)):
        
        nomes_pFrame = img_original_names[img]
        p_frame = cv2.imread(nomes_pFrame, cv2.IMREAD_GRAYSCALE)
        
        img_codificada , vetores = predicao_movimento(i_frame, p_frame)
        
        nome_img_guardada = "InterFrame_compensacao_codificacao/seq3_bola_%02d.jpg"%img
        cv2.imwrite( nome_img_guardada , img_codificada,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        
#        ''' Vizualizar os vetores de movimento '''
#        plt.figure(img)
#        blocosX = largura/16.
#        blocosY = altura/16.
#        plt.title("Vetores de Movimento da imagem " + str("seq3_bola_%02d.jpg"%img))
#        
##         As coordenadas x e y da localização das setas
#        X, Y = np.meshgrid(np.arange(0,blocosX)*16,np.arange(0,blocosY)*16)
#        Y[::-1]
#        
##         Dar o componente x e y dos vetores das setas
#        U = ([vector[0] for vector in vetores])
#        V = [vector[1] for vector in vetores]
#
#        plt.quiver(X,Y,U,V, angles = 'xy', scale_units = 'xy' , scale=1)
#        plt.gca().invert_yaxis()
#
#        nome_vetores =  "InterFrame_compensacao_codificacao/vetores/vetores"+ str(img) + ".png" 
#        plt.savefig(nome_vetores)

        vetor[:,index] = vetores[:,0]
        vetor[:,index +1 ] = vetores[:,1]
        index += 2
        
    return vetor
        
def descodificacaoCompensacaoMovimento(imagens, vetores, qualidade):
    
    nome = img_original_names[0]
    i_frame = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
    idx = 0
    
    taxa_comp = []
    snr = []
    entro = []
    energ = []
    
    for img in range(1,len(imagens)):
        
        vetor = vetores[: , idx:idx+2]
        idx += 2
        
        nome = "InterFrame_compensacao_codificacao/seq3_bola_%02d.jpg"%img
        p_frame = cv2.imread(nome, cv2.IMREAD_GRAYSCALE)
        
        altura , largura = p_frame.shape
        array_zeros = np.zeros(altura * largura)
        array_zeros = array_zeros.reshape(altura, largura)
        
        count = 0
        for col in np.arange(0,altura,16):
            for lin in np.arange(0,largura,16):
                array_zeros[col:col+16 , lin:lin+16] = i_frame[col + int(vetor[count,0]) : col + int(vetor[count,0]) + 16 , lin + int(vetor[count,1]):lin+int(vetor[count,1])+16]
                count += 1
                
        img_descodificada = (array_zeros.astype(float) + (p_frame.astype(float))) - 128.
        
        '''Guardar as imagens '''
        nome_img_guardada = "InterFrame_compensacao_descodificacao/seq3_descodificada_bola_%02d.jpg"%img
        cv2.imwrite( nome_img_guardada , img_descodificada,(cv2.IMWRITE_JPEG_QUALITY,qualidade))
        
        
    for img in range(1,len(imagens)):
        
        
        print("---------------", "seq3_descodificada_bola_%02d.jpg"%img, "---------------")
        
        nome_original = img_original_names[img]
        img_original = cv2.imread(nome_original, cv2.IMREAD_GRAYSCALE)
        
        nome_img_guardada = "InterFrame_compensacao_descodificacao/seq3_descodificada_bola_%02d.jpg"%img
        img_guardada = cv2.imread(nome_img_guardada, cv2.IMREAD_GRAYSCALE)
        
        # Taxa de Compressão
        tc_print = measure_CompressionRatio(nome_original, nome_img_guardada)
        print("Taxa de Compressão:", tc_print)
        taxa_comp.append(tc_print)
        
        # Relação Sinal Ruído
        snr_print = measure_SNR(img_original,img_guardada)
        print("SNR:", snr_print)
        snr.append(snr_print)
        
        # Entropia
        entro_print = measure_Entropy(img_guardada)
        print("Entropia:", entro_print)
        entro.append(entro_print)
        
        # Energia média por píxel
        energ_print = measure_Energy(nome_img_guardada)
        print("Energia:", energ_print)
        energ.append(energ_print) 
        
        if(img == 10):
            print("-------- Acabou a análise dos resultados --------")
        
    return taxa_comp, snr, entro, energ
          
def predicao_movimento(i_frame, p_frame):
    
    idx = 0
    altura , largura = i_frame.shape
    array_final = np.zeros(altura * largura)
    array_final = array_final.reshape(altura, largura)

    vetores_mov = np.zeros(int(((altura*largura)/(16*16))*2))
    vetores_mov = vetores_mov.reshape( int((altura*largura)/(16*16)),2)
    
    for col in np.arange(0,altura,16):
        for lin in np.arange(0,largura,16):
            #Vai procurar, num bloco de 16 por 16 da p frame, o macrobloco mais parecido com este,
            # na i frame
            
            # realizamos a janela de pesquisa [-15, 15]
            #ini[0] -> xmin
            #ini[1] -> ymin
            #fim[0] -> xmax
            #fim[1] -> ymax
            ini = [col - 15, lin - 15]
            fim = [(col + 16) + 15, (lin + 16) + 15]
            
            # criamos o bloco 16x16
            blocoP_16x16 = p_frame[col:col+16, lin:lin+16]
            
            if (ini[0] < 0):
                 ini[0] = 0
            if (ini[1] < 0):        
                 ini[1] = 0
            if (fim[0] > altura):
                 fim[0] = altura
            if (fim[1] > largura): 
                 fim[1] = largura
            
            janela_pesquisa = i_frame[ini[0]:fim[0],ini[1]:fim[1]]
             
            bloco, coluna, linha = full_search(blocoP_16x16, janela_pesquisa, ini[0], ini[1], col, lin)
            #GUARDA O VETOR DE MOVIMENTO ONDE SE ENCONTROU O MACRO BLOCO DA I FRAME MAIS PARECIDO
            vetores_mov[idx] = coluna , linha 
            array_final[col:col+16,lin:lin+16] = bloco
            idx += 1
    
              
    codificado = p_frame.astype(float) - array_final.astype(float) + 128.
    return  codificado , vetores_mov
        
def full_search(bloco_16x16, janela_pesquisa, janela_x, janela_y, Pframex, Pframey):
    
    altura, largura = janela_pesquisa.shape
    minimo = 10**20 
    array = 0
    coluna = 0
    linha = 0
    
    for i in np.arange(altura-15): 
        for j in np.arange(largura-15):
            
            bloco = janela_pesquisa[i:i+16, j:j+16]
            
            # Função que permite realizar o calculo do erro absoluto médio
            # entre ambos os blocos
            diff = MAE(bloco_16x16,bloco)
            
            if (diff < minimo):
                coluna = i
                linha = j
                array = bloco
                minimo = diff
       
    x = janela_x + coluna
    y = janela_y + linha 
    
    coordx = x - Pframex
    coordy = y - Pframey

    return array, coordx, coordy 


t0 = time()
qualidade = 50
vetores_codificacao = codificacaoCompensacaoMovimento(img_ball, qualidade)
t1 = time()
print("Tempo de Codificação Inter-Frame com compensação de movimento: " + str(t1-t0))


t0 = time()
taxa_compr, snr, entropia, energia = descodificacaoCompensacaoMovimento(img_ball, vetores_codificacao, qualidade)
t1 = time()
print("Tempo de Descodificação Inter-Frame com compensação de movimento: " + str(t1-t0))


mostrar_graficos(snr, taxa_compr, entropia, energia)