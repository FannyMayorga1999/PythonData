import pandas as pd 

data01= {'_key1':pd.Series(['KO','K1','K2','K3']),
    '_key2':pd.Series(['z0','z1','z2','z3']),
    'city':pd.Series(['city_0','city_1','city_2','city_3']),
    'user_name':pd.Series(['user_0','user_1','user_2','user_3'])
}

dataFrame01 = pd.DataFrame(data01)
print(dataFrame01)

data02= {'_key1':pd.Series(['KO','K1','K2','K3']),
    '_key2':pd.Series(['z0','z1','z2','z3']),
    'hire_date':pd.Series(['h_0','h_1','h_2','h_3']),
    'profession':pd.Series(['p_0','p_1','p_2','p_3'])
}

dataFrame02 = pd.DataFrame(data02)
#print(dataFrame02)
#pf = pd.concat([dataFrame01,dataFrame01],ignore_index=True))       #une dos datasFrame (concatenar)
                                                                    #ingnore_index dice que debe ser True para llamar a la concat()

#pd = pd.concat([dataFrame01,dataFrame02],axis=1,join='inner')      #imprime lo que tiene en comun

dataFrame02.append(dataFrame01)                                     #union de dos data 

#pt = pd.merge(dataFrame01,dataFrame02,left_on='city', right_on='hire_date')#union de colummnas a colummnas
                                                                    #left_on como el nombre de DataFrame izquierdo y right_oncomo el nombre de DataFrame correcto

pt = pd.merge(dataFrame01,dataFrame02, how='outer')                 #how='outer' combina los resultados de la izquierda y la derecha se une externa. ompletará NaNlas coincidencias faltantes en cada lado.
#print(pt)                                                   

pk = pd.merge(dataFrame01,dataFrame02, how='inner',on='_key2')      #how='inner produce sólo el conjunto de registros que coincidan tanto en trama de datos A y B. 
print(pk)

pr = pd.merge(dataFrame01,dataFrame02, how='right')                 #how='rigth' produce un conjunto completo de registros de trama de datos B
print(pr)                                                           #how='left' produce un conjunto completo de registros de trama de datos A

pf = [dataFrame02,dataFrame01]
df_keys = pd.concat(pf, keys=['x', 'y'],sort=False)                 #definimos las claves para cada una de las tablas
#print(df_keys.loc['y'])                                            #se puede llamar segun la clave

