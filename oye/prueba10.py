import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split           
from sklearn.metrics import mean_squared_error,r2_score
from math import sqrt    

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

data['queue'] = data['queue'].replace(('Servicios Preferenciales','H_EAV','H_CCC','H_CIT','H_INF','H_AMB','H_MAD','M_UIO','H_HOS','H_ACT','H_DEN','M_GYE','H_VEN','M_SAC','M_COR','H_ECA'),1)

data['time'] = data['time'].astype("datetime64[ns]")
data['time'] = data['time'].map(lambda x: x.replace(second=0, minute=0))
data['queue'] = data['queue'].astype("int64")

 
data = data.groupby(['time','date']).sum()

data.fillna(0, inplace=True)

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

data.reset_index(level=0, inplace=True)

mask1 = data['date'] > '2017-01-01'
mask2 = data['date'] < '2019-03-27' 

data = data[mask1 & mask2]

data['date'] = pd.to_datetime(data['date'])
data['date'] = data['date'].astype("int64")

print(data.dtypes)

features = ['queue']
y = data[features]
target = ['date']
x = data[target]

print(x.head())
print(x.shape,y.shape)
X_train, X_test ,  y_train , y_test = train_test_split(x,y , test_size=0.20, random_state=42)
future = LinearRegression()
future.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,normalize=False)
y_prediction = future.predict(X_test).astype("int64")

RMSE = sqrt(mean_squared_error(y_true= y_test,y_pred= y_test)) 

m = future.coef_[0]
b = future.intercept_
y_m = m*x+b
print(y_prediction[:10])


data['date'] = data['date'].astype("datetime64[ns]")
print(data.head(11))

plt.scatter(x,y)
plt.plot(x,y_m, color='red')
plt.xlabel('date')
plt.ylabel('queue')
plt.title('calls per days')
plt.grid()
plt.show()