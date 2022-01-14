# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:22:49 2021

@author: luisc
"""

import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LogisticRegression, Lasso, Ridge
from sklearn.feature_extraction.text import TfidfVectorizer


def LassoRegression(Xtrain,Xtest,y1,y2,penaltyType = "l1",cValue = None):
    lr = LogisticRegression(penalty = "l1",solver = 'saga', C = cValue).fit(Xtrain,y1)
    w =lr.coef_
    idx = np.argsort(w)
    w = w.squeeze()
    idx = idx.ravel()
    scoreTrain = np.round(lr.score(Xtrain, y1) * 100, 3)
    scoreTest = np.round(lr.score(Xtest, y2) * 100, 3)
    print("Número de Erros: ", np.sum(w!=0))
    print("Número de Acertos: ", np.sum(w==0))
    print("Acertos no Treino: " + str(scoreTrain))
    print("Acertos no Teste: " + str(scoreTest))
    y2n = lr.predict(Xtest)
    print("Matriz de Confusão: \n" + str(confusion_matrix(y2, y2n)))
    print("Fim de regularização Lasso\n")
    
    
    
def text2Vector(Xtrain,Xtest,n_grams = (2,2),max_featuresV = None):
    print("Inicialização de converção de texto para vectores.\n")
    tfidf = TfidfVectorizer(ngram_range = n_grams,max_features = max_featuresV).fit(Xtrain)
    voc = tfidf.get_feature_names()
    Xtrain = tfidf.transform(Xtrain)
    Xtest = tfidf.transform(Xtest)
    return Xtrain,Xtest,voc


def classify(Xtrain,Xtest,y1,y2,penaltyType="l1",cValue = None):
    print("Inicialização de classificação\n")
    y1 = (y1 >= 7) * 1.0
    y2 = (y2 >= 7) * 1.0
    
    LassoRegression(Xtrain,Xtest,y1,y2,'l1',cValue)
    print("End of the classify")
    
    
fN = 'imdbFullPorter.p'
D = pickle.load(open(fN,'rb')) 
D.keys() 
dados = D['data']
target = D['target']
X1, X2, y1, y2 = train_test_split(dados[:5],target[:5],test_size=0.3,random_state = 42)
x_train, x_test, Vocab = text2Vector(X1, X2,max_featuresV = 150)
classify(x_train, x_test, y1, y2, penaltyType = 'l1', cValue = 1)
