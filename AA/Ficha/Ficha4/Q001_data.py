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

D=pickle.load(open('A45125_Q001_data.p','rb'))
X=D['X']*1.
y=D['y']

#Pergunta 1 - alinea a)
X=np.vstack((np.ones(X.shape[1]),X))
y = 2 * y - 1

w = np.array([0.00, 0.38, -0.92])
#w = np.array([0.00, 0.91, 0.42])

yh = np.dot(w.T, X)

ypred = (yh > 0 ) * 1
ypred = 2 * ypred - 1 

print(confusion_matrix(y,ypred))
tn, fp, fn, tp =confusion_matrix(y,ypred).ravel()
        
print("True Positive:", tp)
print("False Positive:", fp)
print("True Negative:", tn)
print("False Negative:", fn)
print()

erros0 = 0
for i in range(len(yh)):
    if y[i] == -1 and yh[i] > 0:
        erros0+=1
        
erros1 = 0
for i in range(len(yh)):
    if y[i] == 1 and yh[i] < 0:
        erros1+=1

acertos0 = 0
for i in range(len(yh)):
    if y[i] == -1 and yh[i] < 0:
        acertos0+=1
        
acertos1 = 0
for i in range(len(yh)):
    if y[i] == 1 and yh[i] > 0:
        acertos1+=1

       
print("Numero erros na classe w1",erros1)
print("Numero erros na classe w0",erros0)
print("Numero acertos na classe w0",acertos0)
print("Numero acertos na classe w1",acertos1)
print("Numero total de acertos",acertos0+acertos1)
print("Numero total de erros",erros0+erros1)
print("erro quadratico medio",mean_squared_error(y,yh))
print("Recall:", round((tp)/(tp+fn),3))
print("Falsos Alarmes:", (fp)/(tn+fp))
print()


#Pergunta 1 - alinea a) V F F F
#Pergunta 1 - alinea b) F F F V 
#Pergunta 1 - alinea c) F F V F


