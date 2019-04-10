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
data.fillna(0, inplace=True)
data01 = data.groupby(['date','time']).queue.sum()
df = data01.unstack()
df.fillna(0, inplace=True)
mask1 = df.index > '2019-02-01'
mask2 = df.index < '2019-03-27'

df = df[mask1 & mask2]

pd.options.display.float_format = '{:,.0f}'.format

print(df.head(30))

plt.bar(df.index.values, df[0].values)
plt.xlabel('date')
plt.ylabel(df[0].iloc[0])
plt.title('hours')
plt.show()