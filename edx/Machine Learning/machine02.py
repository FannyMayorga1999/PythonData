from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils            #py -m pip install utils
import pandas as pd
import numpy as np 
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/minute_weather.csv")

sampled_df = data[(data['rowID'])%10 == 0]

sampled_df.describe().transpose()
sampled_df[sampled_df['rain_accumulation']==0].shape
sampled_df[sampled_df['rain_duration']==0].shape

rows_before = sampled_df.shape[0]
sampled_df = sampled_df.dropna()

rows_afther = sampled_df.shape[0]

rows_before - rows_afther


features = ['air_pressure','air_temp','avg_wind_direction','avg_wind_speed',
             'max_wind_direction','max_wind_speed','min_wind_direction','min_wind_speed',
             'relative_humidity']


select_df = sampled_df[features]

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
#parallel_plot(data)

#parallel_plot(P)

parallel_plot(P[P['relative_humidity']< -0.5])                              #dias secos
#parallel_plot(P[P['air_temp']> 0.5])                                        #dias calidos                             
#parallel_plot(P[(P['relative_humidity']>0.5) & (P['air_temp']<0.5)])        #dias frios

plt.show()