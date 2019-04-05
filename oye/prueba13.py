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
data['time'] = data['time'].dt.hour
data = data.groupby(['date','time'],as_index = False).sum()
data.fillna(0, inplace=True)


mask1 = data['date'] > '2019-01-01'
mask2 = data['date'] < '2019-03-27'
data = data[mask1 & mask2]

data['date'] = data['date'].astype("datetime64[ns]")

df = pd.DataFrame(index=data['date'],columns=data['time'])

#df = df.groupby(df.index).sum()
# data01 = pd.DataFrame(index=data['date'], columns=data['time'])
#df = df.groupby(df.index,as_index = False).mean()

print(df.head(30))
#print(data.dtypes)

