import pandas as pd
import matplotlib.pyplot as plt


##pandas(data) serie de tres dimension 
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres','Fanny']),
   'Age':pd.Series([29,50,60,30,29,80,34,95,15,84,45]),
   'Rating':pd.Series([25,25,23,30,29,23,34,40,30,51,46]),
   'Numero':pd.Series([30,30,28,35,34,28,39,45,35,56,51])
}

panda01 = pd.DataFrame(d)

panda01["hola"] =panda01['Age']*2            #hacer otra columna

panda01 = panda01.replace(25,40)             #replaza valores por otros 

#p = panda01.dropna(axis='columns')          #borra especificando que quieres borra de la
#p = panda01.dropna(axis=0)
#print(p)

panda01 =  panda01.fillna(method='ffill')   #reeplaza los datos vacios por uno anterior
#panda01 = panda01.fillna(method='backfill') #reeplaza los datos vacios por uno anterior con uno despues

print(panda01.isnull().any())                #evalua si son valores tienen algo en comun me returna false

print(panda01)

panda01.plot.bar()                           #dibuja un digrama de barras de los dos lados

panda01.plot.box()                           #dibuja un digrama de cajas

panda01.plot.hist()                          #dibuja un digrama de barras

panda01.plot()                               #dibuja un digrama de lineas

#df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df2.plot.bar()

plt.show()
