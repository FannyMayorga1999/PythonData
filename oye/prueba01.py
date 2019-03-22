from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils           
import pandas as pd
import numpy as np 
from itertools import cycle, islice
import matplotlib.pyplot as plt
import datetime as dt
import datetime

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)

data.fillna(0, inplace=True)
data['date'] = pd.to_datetime(data['date']) 
"""
hist_indicator = 'H_INF'
mask2 = data['callid']<32933
#fanny = 'H_CIT'

#mask1 = data['queue'].str.contains(hist_indicator)
#mask2 = data['callid'].str.isin([hist_calling])    

#mask2 = data['queue'].str.contains(fanny) 
data01 = data[ mask2]

#data[mask1]
plt.plot(data01['date'].values, data01['queue'].values)
plt.show()
"""

"""
before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

clean_data = data.copy()

features = ['queue']

select_df = data[features]

kmeans = KMeans(n_clusters=4)

X = StandardScaler().fit_transform(select_df)

kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
labels = kmeans.predict(X)
centers = kmeans.cluster_centers_

plt.plot(data[features].values, data['v'].values)
plt.show()

print(data)"""