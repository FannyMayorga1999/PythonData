import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split           
from sklearn.metrics import mean_squared_error
from math import sqrt


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

y = [1,2,2,4,5,4,6,4,6,7,9,10,11,12,10]

n = len(x)

y = np.array(y)
x = np.array(x)

sumx = sum(x)
sumy = sum(y)

sumx2 = sum(x*x)
sumy2 = sum(y*y)

sumxy = sum(x*y)

promx = sumx/n
promy = sumy/n

m = (sumx*sumy - n*sumxy)/(sumx**2-n*sumx2) 

b = promy - m*promx

print(b,m)

plt.scatter(x, y )
plt.plot(x,m*x+b)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresion lineal')
plt.grid()
#plt.legend()
plt.show()