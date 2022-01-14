from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.datasets import load_diabetes


D=load_diabetes()
x=D.data
y=D.target

Xtrain = x[:201]
ytrain = y[:201]
Xteste = x[201:]
yteste = y[201:]

#Pergunta 2 - alinea a) F F V F
pf = PolynomialFeatures(4).fit(Xtrain)
X1p = pf.transform(Xtrain)[:, 1:]
X2p = pf.transform(Xteste)[:, 1:]

lasso=Lasso(random_state=42,alpha=0.01).fit(X1p,ytrain)
y1h=lasso.predict(X1p)

erro_absoluto_medio = mean_absolute_error(ytrain, y1h)
print("#########Pergunta_A#########")
print('R2(treino): ',lasso.score(X1p,ytrain))
print("Erro absoluto medio", erro_absoluto_medio)

#Pergunta 2 - alinea b) F F F V 
pf = PolynomialFeatures(2).fit(Xtrain)
X1p = pf.transform(Xtrain)[:, 1:]
X2p = pf.transform(Xteste)[:, 1:]
p3 = LinearRegression().fit(X1p, ytrain)
y2h = p3.predict(X2p)
y1h = p3.predict(X1p)  #train

erro_absoluto_medio = mean_absolute_error(yteste, y2h)
erro_quadratico_medio=mean_squared_error(ytrain,y1h)
print()
print("#########Pergunta_B#########")
print("Erro quadratico medio Teste", erro_quadratico_medio)
print("Erro absoluto medio Teste", erro_absoluto_medio)


#Pergunta 2 - alinea c) F F V F
print()
print("#########Pergunta_C#########")
pf = PolynomialFeatures(3).fit(Xtrain)
#X1p = pf.transform(Xtrain)[:, 1:]
X1p = pf.transform(Xtrain)
p2 = LinearRegression().fit(X1p, ytrain)
print("Numero de coeficientes, incluindo  w0, numa regressao polinomial de ordem 3, e igual a ",
     p2.coef_.shape)

pf = PolynomialFeatures(4).fit(Xtrain)
#X1p = pf.transform(Xtrain)[:, 1:]
X1p = pf.transform(Xtrain)
p3 = LinearRegression().fit(X1p, ytrain)
print("Numero de coeficientes, incluindo  w0, numa regressao polinomial de ordem 4, e igual a ",
     p3.coef_.shape) 

#Pergunta 2 - alinea a) F F V F
#Pergunta 2 - alinea b) F F F V 
#Pergunta 2 - alinea c) F F V F

