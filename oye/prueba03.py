from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils            #py -m pip install utils
import pandas as pd
import numpy as np 
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import datetime as dt

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv",parse_dates=True)

data = data.groupby(['date']).sum()

mask1 = data.index < '2019-03-01' 
mask2 = data.index > '2019-01-01'
data = data[mask1 & mask2]

data[(data['rowid'])%10 == 0]

data.describe().transpose

data.fillna(0, inplace=True)

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

features = ['queueid']

select_df = data[features]

X = StandardScaler().fit_transform(select_df.astype(np.float64))

kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
labels = kmeans.predict(X)

labels = kmeans.predict(X)
centers = kmeans.cluster_centers_
"""
def pd_centers(featuresUsed, centers):
    colNames = list(featuresUsed)
    colNames.append('prediction')

    Z = [np.append(A, index)for index, A in enumerate(centers)]

    P= pd.DataFrame(Z, columns=colNames)
    P['prediction'] = P['prediction'].astype(int)
    print(P)
    return P"""
    
data.index = pd.to_datetime(data.index) 


plt.bar(data.index.values, data['queueid'].values)
plt.xlabel('date')
plt.ylabel(data['queueid'].iloc[0])
plt.title('queue')
plt.show()


#print(data.head(5))
#plt.figure(figsize=(15,8)).gca().axes.set_ylim([-3,+3])
#parallel_coordinates(data,'prediction',color=('#FF5733', '#4CFF33', '#335BFF','#C65F0E'))