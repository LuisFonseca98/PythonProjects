import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

#------- EXERCICIO 1 ---------
x_img = cv2.imread("lenac.tif")
def exe1():
    

    cv2.imshow('Original Image', x_img)
    
    print(x_img.dtype)
    print(x_img.shape)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #taxaDeCompresao - reduzir a redundancia dos dados, de forma a armazenar ou
                        #transmitir esses dados de forma eficiente;
    #PSNR: define a relacao entre a maxima energia de um sinal e o ruido
            #MAX - define o valor maximo de um pixel numa imagem
    #0 - preto
    #255 branco

#------ EXERCICIO 2 ---------
    
def compressionRate(img1name, img2name):
    
    sizeO = os.path.getsize(img1name)
    sizeA = os.path.getsize(img2name)
    taxaCompressao = sizeO/sizeA
    
    return taxaCompressao
    
def PSNR(pic1,pic2):

    MSE = np.mean((pic1.astype("uint8") - pic2.astype("uint8")) ** 2 )
    pixMAX = 255.0
    return 20*np.log10(pixMAX) - 10*np.log10(MSE)

def SNR(img1,img2):
    Psinal = np.sum(np.sum((img2*1.0)**2))
    Perro = (np.sum(np.sum(((img2*1.0)-(img1*1.0))**2)))
    return 10*np.log10(Psinal/Perro)
    
def exe2():

    cv2.imwrite('file1.jpg', x_img, (cv2.IMWRITE_JPEG_QUALITY, 80))
    cv2.imwrite('file2.jpg', x_img, (cv2.IMWRITE_JPEG_QUALITY, 10))
    
    # ---------- SNR ------------
    
    imgjpg1 = cv2.imread('file1.jpg')
    imgjpg2 = cv2.imread('file2.jpg')

    SNR1 = SNR(x_img, imgjpg1)
    SNR2 = SNR(x_img, imgjpg2)
    print("SNR lenac.tif -> file1.jpg (jpg80): " + str(SNR1))
    print("SNR lenac.tif -> file2.jpg (jpg10): " + str(SNR2))
    print()

    # ---------- TAXA COMPRESSAO ---------
    
    taxaCompressao1 = compressionRate('lenac.tif', 'file1.jpg')
    taxaCompressao2 = compressionRate('lenac.tif', 'file2.jpg')
    
    print("TAXA DE COMPRESSAO lenac.tif -> file1.jpg (jpg80): " + str(taxaCompressao1))
    print("TAXA DE COMPRESSAO lenac.tif -> file2.jpg (jpg10): " + str(taxaCompressao2))
    print()

    # ---------- PSNR ---------
    
    PSNR1 = PSNR(x_img, imgjpg1)
    PSNR2 = PSNR(x_img, imgjpg2)
    print("PSNR lenac.tif -> file1.jpg (jpg80): " + str(PSNR1))
    print("PSNR lenac.tif -> file2.jpg (jpg10): " + str(PSNR2))
    

#------ EXERCICIO 3 --------
    
def obterGreyscale():
    x_img_g = cv2.cvtColor(x_img, cv2.COLOR_BGR2GRAY)
    return x_img_g


def exe3():
    x_img_g = obterGreyscale()
    cv2.imshow('Gray Image', x_img_g)
    cv2.imwrite('file3.bmp', x_img_g)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#------ EXERCICIO 4 -------
    
def exe4():
    x_img_g = obterGreyscale()
    plt.hist(x_img_g.ravel(), 256, [0, 256])
    niveisCinzento = np.unique(x_img_g).size
    print("Os níveis de cinzento da imagem são: " + str(niveisCinzento))
    
#------ EXERCICIO 5 -------

def exe5():
    x_img_g = obterGreyscale()
    for i in range(8):
        img = np.bitwise_and(x_img_g,2**i)
        cv2.imshow('BW ' +  str(i), (img * 255).astype("uint8"))
        #cv2.imwrite('BW ' + str(i) + '.bmp', (img * 255).astype("uint8"))
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#------ EXERCICIO 6 -------
    
def dithering(img):
    height,width= img.shape
    imgFinal = np.zeros(img.shape, np.uint8)
    for y in range(height-1):
        for x in range(width-1):
            oldPixel = img.item(y,x)
            newPixel = 255 if oldPixel > 127 else 0
            imgFinal.itemset(y,x,newPixel)
            erroQuantizado = oldPixel-newPixel
            img.itemset(y,x+1,img.item(y,x+1) + erroQuantizado * 7/16)
            img.itemset(y+1,x+1,img.item(y+1,x+1) + erroQuantizado * 3/16)
            img.itemset(y+1,x,img.item(y+1,x) + erroQuantizado * 5/16)
            img.itemset(y+1,x-1,img.item(y+1,x-1) + erroQuantizado * 1/16)
    return imgFinal


def exe6():
    
    x_img_g = obterGreyscale()
    y = dithering(x_img_g)
    cv2.imshow('Dither',y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#------ EXERCICIO 7 -------
    
def exe7():
    x_img_g = obterGreyscale()
    y = dithering(x_img_g)
    cv2.imwrite('Dither.bmp', y)
    fileDither = cv2.imread('Dither.bmp')
    
    taxaCompressao = compressionRate('lenac.tif' ,'Dither.bmp')
    snr = SNR(x_img, fileDither)
    psnr = PSNR(x_img, fileDither)
    
    print("TAXA DE COMPRESSAO lenac.tif -> Dither.bmp: " + str(taxaCompressao))
    print("SNR lenac.tif -> Dither.bmp: " + str(snr))
    print("PSNR lenac.tif -> Dither.bmp: " + str(psnr))
    
#------ EXERCICIO 8 -------
    
def monochromeImg(angulo,tamanho):
    width = int(tamanho) 
    height = int(tamanho) 
    radius = angulo * np.pi/180.0
    img = np.zeros((width,height)) 
    for x in range(width): 
        for y in range(height): 
            eixoX = (float) (x - (width/2))
            eixoY = (float) (y - (height/2))
            if eixoX == 0: 
                ang = np.pi/2.
                if eixoY < 0: 
                    ang +=  np.pi 
            else:
                ang = np.arctan(eixoY/eixoX) 
            if(eixoX < 0) & (eixoY < 0):  
                ang=np.arctan(eixoY/eixoX)
            if((eixoX < 0) & (eixoY > 0)): 
                ang += np.pi
            if(eixoX > 0)& (eixoY < 0): 
                ang += 2*np.pi
            if(eixoX < 0) & (eixoY < 0): 
                ang += np.pi
                   
            for i in range(360//angulo): 
                if (radius*i*2 <= ang <= radius*(i*2+1) ):
                    img[y][x] = 255 
    cv2.imshow("img", img)
    print(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite('exe8.bmp', img)

def exe8():

    monochromeImg(1,400)

if __name__ == '__main__':

##    exe1()
##    exe2()
    exe3()
##    exe4()
##    exe5()
##    exe6()
##    exe7()
##    exe8()
