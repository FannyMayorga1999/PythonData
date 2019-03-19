import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
panda01 = pd.DataFrame(d)

print(panda01.describe)
print(panda01)
print(panda01.mean())            #mean devuelve un valor promedio
print(panda01.std())             #devuelve un valor estandar
print(panda01.max())             #returna el mayor 
print(panda01.sum())             #returna la suma todos los valores                  
print(panda01.median())          #devuelve el valor medio 
print(panda01.mode())            #modo de los valores 
print(panda01.min())             #valor minimo       
print(panda01.prod())            #valor producto de la data
print(panda01.corr())            #valor del incremento de la tablas
print(panda01.all())             #me evalua si los datos son veraderos
