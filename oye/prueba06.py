import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt


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

print(data.dtypes)
print(data.head())