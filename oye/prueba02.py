from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np 
import matplotlib.pyplot as plt
import datetime as dt
#import seaborn as sb
from pandas.plotting import parallel_coordinates

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv",parse_dates=True)

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)

data = data.groupby(['queue']).sum()
 
data.fillna(0, inplace=True)

data.describe().transpose()

#mask1 = data['date'] < '2019-03-01' 
#mask2 = data['date'] > '2019-01-01'
#data = data[mask1 & mask2]

#data['date'] = pd.to_datetime(data['date'])



features = ['queueid']

select_df = data[features]

X = StandardScaler().fit_transform(select_df)

kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
labels = kmeans.predict(X)
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

parallel_plot(P)


#print(data.dtypes)
print(data.head(5))

plt.show()
