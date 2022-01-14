# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:32:11 2021

@author: luisc
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


#Para conjuntos de dados mais pequenos, o melhor é o "liblinear", caso foi escolhido "saga" 
#dá jeito para aqueles com um conjunto de dados maior, sendo mais rápido;
#Para problemas em multiclass, o melhor é usar: newton-cg,sag,saga e lbfgs, pois aguentam perda multinomial;
#newton-cg,lbfgs,sag e saga suportam L2(ridge) ou None;
#liblinear e saga suportam L1(lasso); 
#liblinear não suporta penalyType = None;

"""Metodo que calcula a regressao logistica"""
def RegressaoLogistica(Xtrain,Xtest,y1,y2, penaltyType = 'l1',cValue = None, solverType = 'liblinear'):
    gs = None
    tipoRegressao = "Lasso" if penaltyType == "l1" else "Ridge\n" 
    gsMelhorParametro = None
    print("Inicialização de Regressão Logistica ",tipoRegressao)
    if cValue is None:
        if penaltyType == "l1":
            parametros = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
                          'solver':('liblinear','saga')
                          }
            lr = LogisticRegression(penalty=penaltyType,C= cValue,solver = solverType,max_iter=5000)
        elif penaltyType == "l2":
             parametros={'C': [0.001, 0.01, 0.1, 1, 10, 100],
                        'solver' : ('saga','sag', 'lbfgs', 'newton-cg')
                        }
             lr = LogisticRegression(penalty = penaltyType,C= cValue,solver = solverType,max_iter = 5000)
        gs = GridSearchCV(lr, parametros)
        gs.fit(Xtrain,y1)
        gsMelhorParametro = gs.best_params_
        print("O melhor parametro é: ", str(gsMelhorParametro))
    else:
        gs = LogisticRegression(penalty = penaltyType, solver = solverType, C = cValue, max_iter = 5000)
        gs.fit(Xtrain,y1)
        
    scoreTrain = np.round(gs.score(Xtrain, y1) * 100, 3)
    scoreTest = np.round(gs.score(Xtest, y2) * 100, 3)
    
    print("Acertos no Treino: " + str(scoreTrain))
    print("Acertos no Teste: " + str(scoreTest))
    y2n = gs.predict(Xtest)
    print("Matriz de Confusão: \n" + str(confusion_matrix(y2, y2n)))
    print("As classes do Teste são: " + str(y2n))
    print("Regressão Logistica",tipoRegressao,solverType, "concluída")
    
    return scoreTrain,scoreTest
    
"""Metodo que calcula a maquina de suporte vetorial"""
def SVM(Xtrain, Xtest, y1, y2, cValue = None, kernelType = 'None'):
    gs = None
    gsMelhorParametro = None
    print("Inicialização de Máquina de Suporte Vetorial\n")
    if cValue is None and kernelType is None:
        parametros = {
            'C': [0.001, 0.01, 0.1, 1, 10, 100], 
            'kernel' : ('linear', 'rbf', 'sigmoid')
            }
        svm = SVC(gamma = 'auto',max_iter=5000,decision_function_shape='ovr')
        gs = GridSearchCV(svm, parametros)
        gs.fit(Xtrain,y1)
        print("O melhor parametro é: ", str(gsMelhorParametro))
    else:
        gs = SVC(gamma='auto', max_iter= 5000, decision_function_shape='ovr', C = cValue, kernel = kernelType)
        gs.fit(Xtrain,y1)
    
    scoreTrain = np.round(gs.score(Xtrain, y1) * 100, 3)
    scoreTest = np.round(gs.score(Xtest, y2) * 100, 3)
    
    print("Acertos no Treino: " + str(scoreTrain))
    print("Acertos no Teste: " + str(scoreTest))
    y2n = gs.predict(Xtest)
    print("Matriz de Confusão: \n" + str(confusion_matrix(y2, y2n)))
    print("As classes do Teste são: " + str(gs.predict(Xtest)))
    print("Máquina de Suporte Vetorial concluida\n ")
    
    return scoreTrain, scoreTest


"""Metodo que calcula a vizinhanca de KNN"""
def kNN(Xtrain, Xtest, y1, y2, n_neighborsValue = None):
    gs = None
    print("kNN started.")
    if n_neighborsValue == None:
        # Parametros a testar
        print("Yay entrei no none, agora esperas uma eternidade")
        parameters = {
                'n_neighbors': [ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 
                                100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 
                                200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 
                                300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 
                                400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495] 

                }
        knn = KNeighborsClassifier()
        # GridSearch para obter os melhores parametros de classificação
        gs = GridSearchCV(knn, parameters)
        gs.fit(Xtrain, y1)
        print("Melhor parametro: " + str(gs.best_params_))
    else:
        gs = KNeighborsClassifier(n_neighbors = n_neighborsValue)
        gs.fit(Xtrain, y1)
    
    #save_data(gs,save_string)
    print("Train success: " + str(np.round(gs.score(Xtrain, y1) * 100, 3)))
    print("Test success: " + str(np.round(gs.score(Xtest, y2) * 100, 3)))
    y2n = gs.predict(Xtest)
    print("Confusion matrix: \n" + str(confusion_matrix(y2, y2n)))
    print("Test classes: " + str(gs.predict(Xtest)))
    print("kNN Classifier concluded.")
    

def binClassify(Xtrain,Xtest,y1,y2,
                classificatorType = 'logistic lasso', 
                cValue = None, 
                solverType = None, 
                kernelType = None,
                n_neighborsValue=None):
    
    y1 = (y1 >= 7) * 1.0
    y2 = (y2 >= 7) * 1.0
    print("Inicialização da classificação binária\n")    
    classificatorType = classificatorType.lower()
    resultado = 0
    
    if classificatorType == 'logistic lasso': resultado = RegressaoLogistica(Xtrain, Xtest, y1, y2,'l1', cValue, solverType)
    elif classificatorType == 'logistic ridge': resultado = RegressaoLogistica(Xtrain, Xtest, y1, y2,'l2', cValue, solverType)
    elif classificatorType == 'svm': resultado = SVM(Xtrain, Xtest, y1, y2,cValue,kernelType)
    elif classificatorType == 'knn': resultado = kNN(Xtrain, Xtest, y1, y2, n_neighborsValue)
    print("Fim da classificação binária\n")
    return resultado



# =============================================================================
# D = pickle.load(open('imdbFullPorter.p','rb'))   
# Data = D['data']
# Target = D['target']
#     
# X1,X2,y1,y2 = train_test_split(Data,Target,random_state = 42)
# Xtrain,Xtest,Vocabulario = textoSplitTreinoTeste(X1,X2)
# binClassify(Xtrain, Xtest, y1, y2,'logistic lasso',n_neighborsValue=300) 
# =============================================================================
