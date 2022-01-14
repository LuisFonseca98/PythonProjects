import numpy as np
import scipy.spatial.distance as spd
import pickle
from scipy.linalg import sqrtm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split,KFold,StratifiedKFold,cross_val_predict,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import scipy.spatial.distance as spd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge,Lasso
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

D=pickle.load(open('A45125_Q003_data.p','rb'))
x=D['x']*1.
y=D['y']
fold=D['folds']

#Pergunta 3 - alinea a) F F V F

xtrain=x[fold==0]
xteste=x[fold==1]
ytrain=y[fold==0]
yteste=y[fold==1]

pf = PolynomialFeatures(degree=3,include_bias=False).fit(xtrain.reshape(-1, 1))
X1n = pf.transform(xtrain.reshape(-1, 1))[:, 1:]
X2n = pf.transform(xteste.reshape(-1, 1))[:, 1:]
lr = LinearRegression().fit(X1n, ytrain)

yh = lr.predict(X1n)
yh2 = lr.predict(X2n)
print("###################Pergunta_A###################")
print('R2(treino): ',lr.score(X1n,ytrain))
print("Erro Absoluto Medio: ", mean_absolute_error(yteste, yh2))
#print("Erro Quadratico Medio: ", mean_squared_error(ytrain, yh))

print()
#Pergunta 3 - alinea b) F 
Xtrain = x[:116]
ytrain = y[:116]
Xteste = x[116:]
yteste = y[116:]
 
XtrainB = x[fold == 0]
ytrainB = y[fold == 0]
XtesteB = x[fold == 1]
ytesteB = y[fold == 1]

pf = PolynomialFeatures(4).fit(Xtrain.reshape(-1, 1))
X1n = pf.transform(Xtrain.reshape(-1, 1))[:, 1:]
X2n = pf.transform(Xteste.reshape(-1, 1))[:, 1:]
lr = LinearRegression().fit(X1n, ytrain)
yhA = lr.predict(X1n)
yhA2 = lr.predict(X2n)
print("R^2 yhA conjunto treino =", lr.score(X1n, ytrain))
print("R^2 yhA conjunto teste =", lr.score(X2n, yteste))
print("Erro yhA conjunto treino =", np.argwhere(ytrain != yhA).shape)
print("Erro yhA conjunto teste =", np.argwhere(yteste != yhA2).shape)
print("Erro yhA conjunto treino =", np.sum(np.abs(ytrain - yhA)) / yhA.shape[0])
print("Erro yhA conjunto teste =", np.sum(np.abs(yteste - yhA2)) / yhA2.shape[0])
print(np.abs(np.sum(np.abs(ytrain - yhA)) / yhA.shape[0] - np.sum(np.abs(yteste - yhA2)) / yhA2.shape[0]))

pf = PolynomialFeatures(4).fit(XtrainB.reshape(-1, 1))
X1nB = pf.transform(XtrainB.reshape(-1, 1))[:, 1:]
X2nB = pf.transform(XtesteB.reshape(-1, 1))[:, 1:]
lrB = LinearRegression().fit(X1nB, ytrainB)
yhAB = lr.predict(X1nB)
yhA2B = lr.predict(X2nB)
print("R^2 yhB conjunto treino =", lr.score(X1nB, ytrainB))
print("R^2 yhB conjunto teste =", lr.score(X2nB, ytesteB))
print("Erro yhB conjunto treino =", np.sum(np.abs(ytrainB - yhAB)) / yhAB.shape[0])
print("Erro yhB conjunto teste =", np.sum(np.abs(ytesteB - yhA2B)) / yhA2B.shape[0])

Xtrain = x[fold == 0]
Xteste = y[fold == 1]
print("Xtrain shape =", Xtrain.shape)
print("Xteste shape =", Xteste.shape)
ytrain = y[fold == 0]
yteste = y[fold == 1]
print("ytrain shape =", ytrain.shape)
print("yteste shape =", yteste.shape)

#Pergunta 3 - alinea c)F F F V
#teste
pf = PolynomialFeatures(degree=4,include_bias=False).fit(Xtrain.reshape(-1, 1))
X1n = pf.transform(Xtrain.reshape(-1, 1))[:, 1:]
X2n = pf.transform(Xteste.reshape(-1, 1))[:, 1:]
lr = LinearRegression().fit(X1n, ytrain)
lasso=Lasso(random_state=42,alpha=0.01).fit(X2n,yteste)

yh = lr.predict(X1n)
yh2 = lr.predict(X2n)

print("###################Pergunta_C###################")
print('R2(teste): ',lasso.score(X2n,yteste))
print("Erro Quadratico Medio: ", mean_squared_error(yteste, yh2))

#Pergunta 3 - alinea a) F F F V
#Pergunta 3 - alinea b) F F F F
#Pergunta 3 - alinea c) F F F V

