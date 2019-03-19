import pandas as pd
import matplotlib.pyplot as plt


PandasDoc= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")

#print(PandasDoc.loc[33])        #Buscas en .cvs y dato preciso     

#print(PandasDoc.head(5))       #Imprime el numero indicado
#print(type(cantones))          #Formato del archivo


df = pd.DataFrame(PandasDoc)                                                                 
print(df)