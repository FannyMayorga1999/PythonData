import pandas as pd 
from sklearn.model_selection import train_test_split        #selecciona los modelos para su analisis 
from sklearn.tree import DecisionTreeClassifier             #Arbol decisiones de los modelos
from sklearn.metrics import accuracy_score                  #Importamos el clasificador de árboles de decisión.

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

x = clean_data[morning_features].copy()

X_train, X_test ,  y_train , y_test = train_test_split(x,y , test_size=0.33, random_state = 324)

humidy_classifier = DecisionTreeClassifier(max_leaf_nodes = 100,random_state=0)

humidy_classifier.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                    max_features=None,max_leaf_nodes=10, min_impurity_split=7,
                    min_impurity_decrease=0.0, presort=False,random_state=0,
                    splitter='best')

predictions = humidy_classifier.predict(X_test)
print(predictions[:10])

print(y_test['high_humidity_label'][:10])