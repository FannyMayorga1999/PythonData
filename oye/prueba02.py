from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils           
import pandas as pd
import numpy as np 
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

print(type(data['date']))

"""
data['time'] = pd.to_datetime(data['time']) 
data['holdtime'] = pd.to_datetime(data['holdtime'])
data['calltime'] = pd.to_datetime(data['calltime'])
"""
"""

data['time'] = data['time'].astype(np.int64)
data['holdtime'] = data['holdtime'].astype(np.int64)
data['calltime'] = data['calltime'].astype(np.int64)
"""

"""
select_df = data[features]

X = StandardScaler().fit_transform(select_df)

kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
labels = kmeans.predict(X)

#labels = kmeans.predict(X)
centers = kmeans.cluster_centers_

def pd_centers(featuresUsed, centers):
    colNames = list(featuresUsed)
    colNames.append('prediction')

    Z = [np.append(A, index)for index, A in enumerate(centers)]

    P= pd.DataFrame(Z, columns=colNames)
    P['prediction'] = P['prediction'].astype(int)
    return P

def parallel_plot(data):
    plt.figure(figsize=(15,8)).gca().axes.set_ylim([-3,+3])
    parallel_coordinates(data,'prediction',color=('#FF5733', '#4CFF33', '#335BFF','#C65F0E'))

P =  pd_centers(features,centers)


parallel_plot(P[P['relative_humidity']< 'H_INF'])  
"""