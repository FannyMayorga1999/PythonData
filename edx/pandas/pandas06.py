import pandas as pd
import matplotlib.pyplot as plt

##pandas(data) serie de tres dimension 
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres','Fanny']),
   'Age':pd.Series([29,50,60,30,29,80,34,95,15,84,45]),
   'Rating':pd.Series([25,25,23,30,29,23,34,40,30,51,46]),
}

panda01 = pd.DataFrame(d)

panda01["Numero"] =panda01['Age']*2            

panda01.groupby('Rating').mean()

print(panda01)

panda01.plot.bar()                          

plt.show()