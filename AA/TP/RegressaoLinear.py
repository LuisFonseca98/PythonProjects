# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:15:00 2021

@author: luisc
"""
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import PolynomialFeatures

"""Método que calcula a regressão linear"""
def RegressaoLinear(Xtrain,Xtest,y1,y2):
    print("Inicio da regressão linear \n")
    lr = LinearRegression().fit(Xtrain,y1)
    scoreTrain = np.round(lr.score(Xtrain,y1),2)
    scoreTest = np.round(lr.score(Xtest,y2),2)
    print("Resultado do coeficiente R2 da classe Treino: ",str(scoreTrain))
    print("Resultado do coeficiente R2 da classe Treino: ",str(scoreTest))
    
"""Método que calcula a regressao linear com Lasso"""
def RegressaoLinearLasso(Xtrain,Xtest,y1,y2,alpha = None):
    gs = None
    print("Inicio do Lasso \n")
    if alpha is None:
        print("Yay entrei no none")
        parametros = {'alpha':[0.001,0.01,0.1,1,10,10,1000]}
        lasso = Lasso(max_iter=5000)
        gs = GridSearchCV(lasso,parametros).fit(Xtrain,y1)
        print("Melhor parametro: " + str(gs.best_params_))
    else:
        gs = Lasso(alpha,max_iter=5000).fit(Xtrain,y1)
    
    scoreTreino = np.round(gs.score(Xtrain,y1),2)
    scoreTeste = np.round(gs.score(Xtest,y2),2)
    
    print("Resultado do coeficiente R2 da classe Treino: ",scoreTreino)
    print("Resultado do coeficiente R2 da classe Teste: ",scoreTeste)
    
    return scoreTreino,scoreTeste

"""Método que calcula a regressao linear com Ridge"""
def RegressaoLinearRidge(Xtrain,Xtest,y1,y2,alpha = None):
    gs = None
    print("Inicio do Ridge \n")
    
    if alpha is None:
        parametros = {'alpha':[0.001,0.01,0.1,1,10,10,1000]}
        ridge = Ridge(max_iter=5000)
        gs = GridSearchCV(ridge,parametros).fit(Xtrain,y1)
        print("Melhor parametro: " + str(gs.best_params_))
    else:
        gs = Ridge(alpha,max_iter=5000).fit(Xtrain,y1)
    
    scoreTreino = np.round(gs.score(Xtrain,y1),2)
    scoreTeste = np.round(gs.score(Xtest,y2),2)
    
    print("Resultado do coeficiente R2 da classe Treino: ",scoreTreino)
    print("Resultado do coeficiente R2 da classe Teste: ",scoreTeste)
    
    return scoreTreino,scoreTeste
    
    
"""Método que calcula o SVR"""
def MaquinaSuporteVetorialLinear(Xtrain,Xtest,y1,y2,cValue = None,kernelType = 'rbf'):
    gs = None
    print("Inicio do SVR \n")
    if cValue == None and kernelType == None:
        parametros = {
            'C': [0.001, 0.01, 0.1, 1, 10, 100], 
            'kernel' : ( 'libnear','rbf', 'poly')
            }
        svr = SVR(gamma = 'auto',max_iter=5000)
        gs = GridSearchCV(svr,parametros).fit(Xtrain,y1)
        print("Melhor parametro: " + str(gs.best_params_))
    else:
        gs = SVR(gamma = 'auto',max_iter=5000, C = cValue,kernel = kernelType).fit(Xtrain,y1)
    scoreTreino = np.round(gs.score(Xtrain,y1),2)
    scoreTeste = np.round(gs.score(Xtest,y2),2)
    
    print("Resultado do coeficiente R2 da classe Treino: ",scoreTreino)
    print("Resultado do coeficiente R2 da classe Teste: ",scoreTeste)
    
    return scoreTreino,scoreTeste



def classificadorRegressao(Xtrain,Xtest,y1,y2,binario = True, 
                           tipoClassificador = "regressao linear",
                           alpha = None,
                           cValue = None,
                           kernelType = 'rbf'):
    
    if binario:
        y1 = (y1 >= 7) * 1.0
        y2 = (y2 >= 7) * 1.0
        
    tipoClassificador = tipoClassificador.lower()
    resultado = 0
    
    if tipoClassificador == 'regressao linear': resultado = RegressaoLinear(Xtrain, Xtest, y1, y2)
    elif tipoClassificador == 'regressao ridge': resultado = RegressaoLinearRidge(Xtrain, Xtest, y1, y2,alpha)
    elif tipoClassificador == 'regressao lasso': resultado = RegressaoLinearLasso(Xtrain, Xtest, y1, y2,alpha)
    elif tipoClassificador == 'svr': resultado = MaquinaSuporteVetorialLinear(Xtrain, Xtest, y1, y2, cValue,kernelType)
    print("Fim da classificação Regressao Linear \n")
    return resultado
    