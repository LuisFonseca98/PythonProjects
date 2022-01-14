# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:38:57 2021

@author: luisc
"""

import pickle
from TextoParaVetores import text_to_vector
from classificadorBinario import RegressaoLogistica,SVM,kNN,binClassify
from classificadorMulti import RegressaoLogistica,SVM,KNN,multiClassify
from RegressaoLinear import RegressaoLinear,RegressaoLinearLasso,RegressaoLinearRidge,MaquinaSuporteVetorialLinear,classificadorRegressao
from sklearn.model_selection import train_test_split


#fN = 'imdbFullCleaned.p';
#fN = 'imdbFullLancaster.p' 
fN = 'imdbFullPorter.p'
#fN = 'imdbFullSnowball.p'

D = pickle.load(open(fN,'rb')) 
D.keys() 
dados = D['data']
target = D['target']

X1, X2, y1, y2 = train_test_split(dados,target,test_size=0.3,random_state = 42)
#x_train, x_test, Vocab = textoSplitTreinoTeste(X1, X2)


x_train, x_test, ytrain, ytest , voc2 = text_to_vector(X1, X2, y1, y2, n_grams = (1,3))

#classificadoresBin = ['logistic lasso','logistic ridge','svm','knn']
#print("-----------------------LOGISTIC lasso - liblinear---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[0],cValue = 1, solverType = 'liblinear')
#print()
#print("-----------------------LOGISTIC lasso - saga---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[0],cValue = 1, solverType = 'saga')
#print()
#print("-----------------------LOGISTIC ridge - lbfgs---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[1], cValue = 10, solverType = 'lbfgs')
#print()
#print("-----------------------LOGISTIC ridge - saga---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[1], cValue = 10, solverType = 'saga')
#print()
#print("-----------------------LOGISTIC ridge - sag---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[1], cValue = 10, solverType = 'sag')
#print()
#print("-----------------------LOGISTIC ridge - newton-cg---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[1], cValue = 10, solverType = 'newton-cg')
#print("-----------------------SVM - linear---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[2], cValue = 1, kernelType = 'linear')
#print()
#print("-----------------------SVM - linear---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[2], cValue = 1, kernelType = 'linear')
#print()
#print("-----------------------SVM - rbf---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[2], cValue = 1, kernelType = 'rbf')
#print()
#print("-----------------------SVM - sigmoid---------------------------")
#binClassify(x_train, x_test, y1, y2,classificadoresBin[2], cValue = 1, kernelType = 'sigmoid')
#print("-----------------------knn---------------------------")
#binClassify(Xtrain2, Xtest2, y1, y2,classificadoresBin[3], n_neighborsValue = None)


#classificadoresMulti = ['logistic lasso','logistic ridge','svm','knn']
#----------------------------MULTICLASSE---------------------
# =============================================================================
# print("-----------------------LOGISTIC lasso - saga---------------------------")
# multiClassify(x_train, x_test, y1, y2,classificadoresMulti[0],cValue = 1, solverType = 'saga')
# print()
# print("-----------------------LOGISTIC ridge - lbfgs---------------------------")
# multiClassify(x_train, x_test, y1, y2,classificadoresMulti[1], cValue = 10, solverType = 'lbfgs')
# print()
# print("-----------------------LOGISTIC ridge - saga---------------------------")
# multiClassify(x_train, x_test, y1, y2,classificadoresMulti[1], cValue = 10, solverType = 'saga')
# print()
# print("-----------------------LOGISTIC ridge - sag---------------------------")
# multiClassify(x_train, x_test, y1, y2,classificadoresMulti[1], cValue = 10, solverType = 'sag')
# print()
# print("-----------------------LOGISTIC ridge - newton-cg---------------------------")
# multiClassify(x_train, x_test, y1, y2,classificadoresMulti[1], cValue = 10, solverType = 'newton-cg')
# =============================================================================
#print("-----------------------SVM - linear---------------------------")
#multiClassify(x_train, x_test, y1, y2,classificadoresMulti[2], cValue = 1, kernelType = 'linear')
#print("-----------------------SVM - rbf---------------------------")
#multiClassify(x_train, x_test, y1, y2,classificadoresMulti[2], cValue = 1, kernelType = 'rbf')
#print()
#print("-----------------------SVM - sigmoid---------------------------")
#multiClassify(x_train, x_test, y1, y2,classificadoresMulti[2], cValue = 1, kernelType = 'sigmoid')
#print("-----------------------knn---------------------------")
#multiClassify(Xtrain2, Xtest2, ytrain, ytest,classificadoresMulti[3], n_neighborsValue = None)


#----------------------------Regressao Linear---------------------
# =============================================================================
# print("-----------------------Regressao Linear(bin)--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= True, tipoClassificador = 'regressao linear',alpha = None)
# print()
# print("-----------------------Regressao Linear-Lasso(bin)--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= True, tipoClassificador = 'regressao lasso',alpha = None)
# print()
# print("-----------------------Regressao Linear-ridge(bin)--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= True, tipoClassificador = 'regressao ridge',alpha = None)
# print()
# =============================================================================
print("-----------------------Regressao Linear-svr(bin)--------------------------")
classificadorRegressao(x_train,x_test,y1,y2,binario= True, tipoClassificador = 'svr',cValue = 1000, kernelType='rbf')


# =============================================================================
# print("-----------------------Regressao Linear--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= False, tipoClassificador = 'regressao linear',alpha = None)
# print()
# print("-----------------------Regressao Linear-Lasso(--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= False, tipoClassificador = 'regressao lasso',alpha = None)
# print()
# print("-----------------------Regressao Linear-ridge--------------------------")
# classificadorRegressao(x_train,x_test,y1,y2,binario= False, tipoClassificador = 'regressao ridge',alpha = None)
# print()
# =============================================================================
print("-----------------------Regressao Linear-svr--------------------------")
classificadorRegressao(x_train,x_test,y1,y2,binario= False, tipoClassificador = 'svr',cValue = 1000, kernelType='rbf')


