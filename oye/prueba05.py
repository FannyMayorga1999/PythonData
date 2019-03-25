from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sb
from pandas.plotting import parallel_coordinates

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv",parse_dates=True)

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)

#data = data.groupby(['date']).sum()

data['date'] = pd.to_datetime(data['date']) 

data.fillna(0, inplace=True)

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

mask1 = data['date'] < '2019-03-01' 
mask2 = data['date'] > '2019-01-01'
data = data[mask1 & mask2]
sb.factorplot(data.index,data=data,kind="count", aspect=3)

y = data[['queue']].copy()
morning_features = ['date']

x = data[morning_features].copy()

X_train, X_test ,  y_train , y_test = train_test_split(x,y , test_size=0.33, random_state = 324)

future = DecisionTreeClassifier(max_leaf_nodes = 100,random_state=0)

future.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                    max_features=None,max_leaf_nodes=10, min_impurity_split=7,
                    min_impurity_decrease=0.0, presort=False,random_state=0,
                    splitter='best')

predictions = future.predict(X_test)
predictions[:20]

"""plt.bar(values, data['queueid'].values)
plt.xlabel('date')
plt.ylabel(data['queueid'].iloc[0])
plt.title('queue')
plt.show()
"""



plt.show()