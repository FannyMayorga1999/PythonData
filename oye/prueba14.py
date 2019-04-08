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
data['time'] = data['time'].map(lambda x: x.replace(second=0, minute=0))
data['time'] = data['time'].dt.hour
data = data.groupby(['time','date'],as_index = False).sum()
data.reset_index(level=0, inplace=True)
data.fillna(0, inplace=True)


mask1 = data['date'] > '2019-02-01'
mask2 = data['date'] < '2019-03-27'
data = data[mask1 & mask2]

data02 = np.array([data['queue']]*587)
data01 = pd.DataFrame(data02,index=data['time'],columns=data['date'])

data01 = data01.groupby(data01.index).mean()

#data.set_index(['time','date' ], inplace=True)

#data.index = data.index.astype("datetime64[ns]")

#data.loc[len(data)]=['queue'] 

#data = pd.DataFrame(data01,index=data['time'],columns=data.index)
#df = df.fillna(0) 


#df = df.groupby(df.index).sum()
# data01 = pd.DataFrame(index=data['date'], columns=data['time'])
#df = df.groupby(df.index,as_index = False).mean()

print(data.head(10))
print(data01.head(10))
print(data01.shape)


