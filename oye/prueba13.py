import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression          
from sklearn.metrics import mean_squared_error,r2_score
from math import sqrt    

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

data['queue'] = data['queue'].replace(('Servicios Preferenciales','H_EAV','H_CCC','H_CIT','H_INF','H_AMB','H_MAD','M_UIO','H_HOS','H_ACT','H_DEN','M_GYE','H_VEN','M_SAC','M_COR','H_ECA'),1)
data['queue'] = data['queue'].astype("int64")
data['date'] = data['date'].astype("datetime64[ns]")
data['time'] = data['time'].astype("datetime64[ns]")
#data['time'] = data['time'].map(lambda x: x.replace(second=0, minute=0))
data['time'] = data['time'].dt.hour
data = data.groupby(['date','time']).sum()
data.fillna(0, inplace=True)


mask1 = data['date'] > '2019-01-01'
mask2 = data['date'] < '2019-03-27'
data = data[mask1 & mask2]

data['date'] = data['date'].astype("datetime64[ns]")
data01 = np.array([data['queue']]*1271).T

df = pd.DataFrame(data01,index=data['date'],columns=data['time'])
#df = df.fillna(0) 

#pandas.concat([df['foo'].dropna(), df['bar'].dropna()]).reindex_like(df)
#df = df.groupby(df.index).sum()
# data01 = pd.DataFrame(index=data['date'], columns=data['time'])
#df = df.groupby(df.index,as_index = False).mean()

print(data.head(10))
print(df.head(10))
print(df.shape)
#print(data.dtypes)

