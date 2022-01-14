# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:55:42 2021

@author: luisc
"""

import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
from sklearn.model_selection import train_test_split


def limpezaTexto(dadosOriginais):
    print("Inicio da limpeza do texto \n")
    Data = [doc.replace('<br />',' ') for doc in dadosOriginais]#substituir as mudanças de linha
    Data2 = [re.sub(r'[^a-zA-Z]+', ' ',doc)for doc in Data]#tirar tudo que não é caracteres alfabeticos fora
    print("Foi finalizada a limpeza do texto \n")
    return Data2


def aplicarStemming(dadosOriginais,stemType="lancaster", language = "english"):
    stemmers = {"porter": PorterStemmer(),
            "snowball": SnowballStemmer("english"),
            "lancaster": LancasterStemmer()}
    stemmer = stemmers[stemType.lower()]
    print("Inicialização de stemming:",stemType,"Stemmer\n")
    novosDados = [" ".join([stemmer.stem(word) for word in text.split()]) for text in dadosOriginais]
    print("Stemming feito.\n")
    return novosDados


def guardarTexto(Data,Target,stemType):
    D = {'data' : Data,'target' : Target}
    print("A escrever os dados no ficheiro.\n")
    pickle.dump(D, open('imdbFull' + str(stemType) + '.p', 'wb')) 
    print("Os dados foram guardados no ficheiro com sucesso.\n")
    

def text_to_vector(Xtrain,Xtest,ytrain, ytest, min_doc_freq = 5, language = 'english',n_grams = (1,1)):
#def textoSplitTreinoTeste(Xtrain,Xtest,min_doc_freq = 5, language = 'english'):
    print("Converting text into vectors.")
    pattern = r'\b\w\w\w\w+\b' if n_grams == (1,1) else r'\b\w\w+\b'
    #pattern = r'\b\w\w+\b'
    tfidf = TfidfVectorizer(min_df = min_doc_freq, token_pattern = pattern, ngram_range = n_grams, stop_words = language)
    #tfidf = TfidfVectorizer(min_df = min_doc_freq, token_pattern = pattern, stop_words = language)
    tfidf.fit(Xtrain)
    voc = tfidf.get_feature_names()
    #Projecção dos vectores
    x_train = tfidf.transform(Xtrain)
    x_test = tfidf.transform(Xtest)
    print("Finished conversion.")
    return x_train, x_test, ytrain, ytest, voc

#if __name__ == '__main__':
    #D=pickle.load(open('imdbCriticas.p','rb'))
    #Data=D['data']
    #Target=D['target']
    #stemType = "Lancaster"
    #novosDados = limpezaTexto(Data)
    #novosDadosStemming = aplicarStemming(novosDados,stemType)
    #guardarTexto(novosDados, Target, "Cleaned")
    #x_train, x_test, y1, y2 = train_test_split(Data, Target)    
    #x_train2, x_test2, voc2 = textoSplitTreinoTeste(Data[:50],Data[50:150], n_grams = (1,3))
    #x_train2, x_test2, voc2 = text_to_vector(Data[:50],Data[50:150])
