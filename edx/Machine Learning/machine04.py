import pandas as pd 
from sklearn.model_selection import train_test_split        #selecciona los modelos para su analisis 
from sklearn.tree import DecisionTreeClassifier             #Arbol decisiones de los modelos
from sklearn.metrics import accuracy_score                  #Importamos el clasificador de árboles de decisión.
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np


data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/daily_weather.csv")

data[data.isnull().any(axis=1)]                             #limpía la data de valores nulos
data['number']

before_rows = data.shape[0]                                 #guardamos los datos dentro de una variables 

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

clean_data = data.copy()

clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm']>24.99)*1   #agrega un nuevo campo para calcular el mas alto de 25  esto regresa un dato true o false 

y = clean_data[['high_humidity_label']].copy()


morning_features = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','max_wind_speed_9am','max_wind_direction_9am','rain_accumulation_9am','rain_duration_9am']

select_df = clean_data[morning_features]

X = StandardScaler().fit_transform(select_df)

kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
labels = kmeans.predict(X)

#labels = kmeans.predict(X)
centers = kmeans.cluster_centers_

print(clean_data.columns)

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

P =  pd_centers(morning_features,centers)

#parallel_plot(data)

#parallel_plot(P)

#parallel_plot(P[P['']])                              #dias secos
parallel_plot(P)                                        #dias calidos                             
#parallel_plot(P[(P['relative_humidity']>0.5) & (P['air_temp']<0.5)])        #dias frios

plt.show()