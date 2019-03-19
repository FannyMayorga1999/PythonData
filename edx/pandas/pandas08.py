import pandas as pd 

data01= {'_key1':pd.Series(['KO','K1','K2','K3']),
    '_key2':pd.Series(['z0','z1','z2','z3']),
    'city':pd.Series(['city_0','city_1','city_2','city_3']),
    'user_name':pd.Series(['user_0','user_1','user_2','user_3'])
}

data02= {'_key1':pd.Series(['KO','K1','K2','K3']),
    '_key2':pd.Series(['z0','z1','z2','z3']),
    'hire_date':pd.Series(['h_0','h_1','h_2','h_3']),
    'profession':pd.Series(['p_0','p_1','p_2','p_3'])
}

dataFrame01 = pd.DataFrame(data01)
dataFrame02 = pd.DataFrame(data02)

pt = pd.merge(dataFrame01,dataFrame02, how='outer')  

print(pt)
#print(pt['city'].str.split('_'))                   #str.split imprime la consulta eliminando el caracter selecionado ademas de separarlo por una coma
#print(pt['city'].str.contains('2'))                #str.contains evalua si el caracter se encuentra dentro de la data y me regresa un booleano 
#print(pt['city'].str.replace('_','-'))             #str.replace replaza el character selecionado por otro caracter escogido   

print(pt['city'].str.extract('(\w{0,})'))           #extrae uno o varios caracteres de campo escogido
print(pt['city'].str.extract('(\d)'))                   