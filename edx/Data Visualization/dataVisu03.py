import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")
             
    
"""mask1 = data['sex'].str.contains('female')                  #evalua si estan dentro de la data y si encuentra de devuelve true
mask2 = data['sex'].str.contains('male') 
mask3 = data['age']     

stage = data[mask1 & mask2]"""
panda01 = pd.DataFrame(data)

panda01.plot.bar()  
plt.show()

#print(stage.head())

  