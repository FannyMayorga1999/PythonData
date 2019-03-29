import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split           
from sklearn.metrics import mean_squared_error
from math import sqrt   
from sklearn.preprocessing import StandardScaler 
from pandas.plotting import parallel_coordinates   

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv",parse_dates=True)

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)

data = data.groupby(['date']).sum()

data.fillna(0, inplace=True)

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

data.reset_index(level=0, inplace=True)

mask1 = data['date'] < '2019-03-01' 
mask2 = data['date'] > '2018-01-01'

data = data[mask1 & mask2]

features = ['date']

y = data[features].copy()

data['date'] = pd.to_datetime(data['date'])

data['date'] = data['date'].astype("int64")

features = ['queueid']

y = data[features]

target = ['date']

x = data[target]

X_train, X_test ,  y_train , y_test = train_test_split(x,y , test_size=0.20, random_state = 324)

future = LinearRegression()

future.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True,n_jobs=True, normalize=False)

y_prediction = future.predict(X_test)
y_test01 = future.predict(X_train)

print(y_prediction[:10])
print(y_test01[:10])


#print(y_prediction)

RMSE = sqrt(mean_squared_error(y_true= y_test,y_pred= y_prediction))
RMSE01 = sqrt(mean_squared_error(y_true= y_train,y_pred= y_test01))

data['date'] = data['date'].astype("datetime64[ns]")
print(data.head())
print(RMSE)
print(RMSE01)


"""plt.bar(data['date'].values,data['queueid'].values)


future = DecisionTreeClassifier(max_leaf_nodes = 100,random_state=0)

future.fit(X_train, y_train)
predictions = future.predict(X_test)
"""
#data['predictions'] = data[predictions]
#print(predictions)

#print(data.columns)

plt.show()
"""
future = LinearRegression()

future.fit(X_train, y_train



predictions = future.predict(X_test)
predictions[:20]
print(data.dtypes)
print(data.head())

"""

