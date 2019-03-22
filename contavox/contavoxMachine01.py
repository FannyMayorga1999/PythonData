import pandas as pd 
from sklearn.model_selection import train_test_split        #selecciona los modelos para su analisis 
from sklearn.tree import DecisionTreeClassifier             #Arbol decisiones de los modelos
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates



data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv",index_col=0, parse_dates=['date','time','holdtime'])

data.drop(['contactid','firstname','lastname','companyid',	'legalname','tradename','entity','callgrade'], axis='columns', inplace=True)

#data.fillna(1.0, inplace=True)                        #reemplaza los valores nulos

before_rows = data.shape[0]                               

data = data.dropna()

afther_rows = data.shape[0]

before_rows - afther_rows

clean_data = data.copy()



#clean_data['calltime'] = (clean_data['holdtime']>'0:00:03')

Y = clean_data[['reasonid']].copy()

features = ['date','time','holdtime','calltime']

X = clean_data[features].copy()
#data['date01'] = pd.to_datetime(data.date)
data['col_name'] = pd.to_numeric(data['date'], errors='coerce')

X_train, X_test ,  y_train , y_test = train_test_split(X,Y , test_size=0.33, random_state = 324)

humidy_classifier = DecisionTreeClassifier(max_leaf_nodes = 1000,random_state=0)
humidy_classifier.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                    max_features=None,max_leaf_nodes=10, min_impurity_split=7,
                    min_impurity_decrease=0.0, presort=False,random_state=0,
                    splitter='best')

predictions = humidy_classifier.predict(X_test)
print(predictions[:10])

print(y_test['high_humidity_label'][:10])

def parallel_plot(data):
    plt.figure(figsize=(15,8)).gca().axes.set_ylim([-3,+3])
    parallel_coordinates(data,'prediction',color=('#FF5733', '#4CFF33', '#335BFF','#C65F0E'))


parallel_plot(data[data['holdtime']< -0.5])