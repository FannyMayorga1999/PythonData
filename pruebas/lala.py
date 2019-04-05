from datetime import datetime
import pandas as pd
import numpy as np
import pandas_datareader.data as web

start = pd.Timestamp ('1950-01-01')
end = pd.Timestamp ('2016-01-04')
f = web.DataReader ('^GSPC', 'yahoo',start,end)

f = f.loc[f.index.month == 11,'Close']

#Creamos un data-frame vacío solo con las columnas(dia/mes) y los indices(años) 
inicio = pd.Timestamp('2016-11-01')
final = pd.Timestamp('2016-11-30')
columnas = [datetime.strftime(timestamp, '%d/%m') for timestamp in pd.date_range(inicio, final, freq="1D")]
indices = [datetime.strftime(timestamp, '%Y') for timestamp in pd.date_range(start, end, freq="A")]
df = pd.DataFrame(index=indices, columns=columnas)
df = df.astype("float") 


#LLenamos el data-frame nuevo con los datos que nos retorna el filtrado con .loc
for fecha in f.index:
    fila = str(fecha.year)
    columna = datetime.strftime(fecha, '%d/%m')
    df.set_value(fila, columna, f[fecha])