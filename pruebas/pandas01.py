# install py -m pip install pandas

import pandas as pd

#pandas(data) serie de una dimension 
panda01 =  pd.Series(data=[100,200,300,400])
#print(panda01)


panda02 =  pd.Series(data=[100,200,300,400], index=['Casillas', 'Ramos', 'Pique', 'Puyol'])
panda02 *2
#print(panda02)                       
#print(panda02.index['Casillas', 'Ramos'])  #se puede ingresar solo me array o data 

panda03 = pd.Series(
    {1: 'Martes', 
    2: 'Lunes', 
    3:'Miercoles', 
    4:'Jueves', 
    5:'Viernes', 
    6: 'Sabado',
    7: 'Domingo'}
)
#print(panda03[1])                          #busqueda de dato 
#print(panda02.loc['Casillas'])              #busqueda de datos evaluando si esta por el index 
#print('Ramos' in panda02)                   #evalua si el elemento esta dentro de la data 


panda04 = name_age = {
    'Name' : ['Bill', 'ALICIA', 'David', 'Hany', 'Ibtisam'],
    'Age' : [32, 55, 20, 43, 30]}           #(tabla) de un diccionario de listas


panda05 = pd.DataFrame(panda03)
#print(panda05)

##pandas(data) serie de dos dimension 
panda06 = {
    'data01':pd.Series(data=[100,200,300,400], index=['Casillas', 'Ramos', 'Pique', 'Puyol']),
    'data02':pd.Series(data=[500,600,700,800,900], index=['Casillas', 'Ramos', 'Mera', 'Vera','Mayorga'])
    }
p = pd.DataFrame(panda06)                   #DataFrame hace que la data se haga tablas

#print(p.columns)                           #para imprimir solo las columnas
p['Boleano'] = p['data01'] > 200            #condicion para evaluar si es mayor a 200 

print(p)


panda07 =(
    { 'Martes':1, 
    'Lunes':2, 
    'Miercoles':3, 
    'Jueves':4, 
    'Viernes':5, 
    'Sabado':6,
    'Domingo':7},
    { 'Enero':1, 
    'Febrero':2, 
    'Marzo':3, 
    'Abril':4,
    'Domingo':7,
     'Lunes':2}
)
#print(pd.DataFrame(panda07))
#print(pd.DataFrame(panda07, index=['hola', 'XD'] )) #se le asigna un nombre para los campos del index
#print(pd.DataFrame(panda07, columns=['Domingo','Marzo','Lunes'] ))

