import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random 

data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")
print(data.shape)

#print(data.head(10))
df = pd.DataFrame(data)

years = data['Year'].unique().tolist() #convertimos los datos un arreglo(lista) y unique para no hacer copias
#for i in countries:
#    print (i)

print(min(years)," to ",max(years))

#print(df)
