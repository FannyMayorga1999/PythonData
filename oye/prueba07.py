import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split           
from sklearn.metrics import mean_squared_error,r2_score
from math import sqrt    

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)



data['queue'] = data['queue'].replace(('Servicios Preferenciales','H_EAV','H_CCC','H_CIT','H_INF','H_AMB','H_MAD','M_UIO','H_HOS','H_ACT','H_DEN','M_GYE','H_VEN','M_SAC','M_COR','H_ECA'),1)

data['queue'] = data['queue'].astype("int64")
 
data = data.groupby(['date']).sum()

#data.fillna(0, inplace=True)

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

data.reset_index(level=0, inplace=True)

mask1 = data['date'] < '2019-03-27' 
mask2 = data['date'] > '2010-01-01'

data = data[mask1 & mask2]

data['date'] = pd.to_datetime(data['date'])

data['date'] = data['date'].astype("int64")

features = ['queue']

y = data[features]

target = ['date']

x = data[target]

X_train, X_test ,  y_train , y_test = train_test_split(x,y , test_size=0.10, random_state = 324)

future = LinearRegression()

future.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True,n_jobs=True, normalize=False)


"""future = DecisionTreeClassifier(max_leaf_nodes = 10000,random_state=0)

future.fit(X_train, y_train)"""


y_prediction = future.predict(X_test).astype("int64")
y_test01 = future.predict(X_train).astype("int64")

print(y_prediction[:10])
print(y_test01[:10])

RMSE = sqrt(mean_squared_error(y_true= y_test,y_pred= y_test)) 
RMSE01 = sqrt(mean_squared_error(y_true= y_train,y_pred= y_test01))



data['date'] = data['date'].astype("datetime64[ns]")



m = future.coef_[0]
b = future.intercept_
y_m = m*x+b

plt.scatter(x,y)
plt.plot(x,y_m, color='red')
plt.xlabel('date')
plt.ylabel('queue')
plt.title('calls per days')
plt.grid()
plt.show()
