

import numpy as np

matrizRandom = 10 + np.random.random((4,5)) 
#print(matrizRandom)

matrir01 = np.arange(15).reshape(3, 5)  #metodo estadistico para sacar la desviación estándar de una matriz
print(matrir01.mean(axis = -1))         #desviación estándar(datos se extienden sobre un rango de valores más amplio.)
#print(matrir01)                         #axis me ayuda a sacar la columna central siendo que es positivo y si en negativo me saca la fila


arr = np.empty((8, 3))                  #for para llenar la matriz 
for i in range(8): 
    arr[i] = i
#print(arr)


arr01 = np.arange(24).reshape((6, 4))    #define los elementos dentro del matriz arange
#print(arr01)                            #reshape de fine las columnas y filas 


arr02 = np.arange (24) .reshape ((2, 3, 4)) #el primer numero define en cuantas matrices la vamos hacer 
                                            #el segundo file y el tercero columnas pero los tres siempre me tiene que dar el range<
#arr02.transpose ((1, 0, 2))
arr02.swapaxes(1,1)                         # define los elementos dentro del matriz arange por prioridad
#print(arr02) 


arr03 =  np.random.random((4,5))            #me dan numeros aletorios entre  0 / 1
print(arr03)

print(arr03.sum())                          #suma todos los elementos dentro de la matriz

arr04 =  np.random.randn(20)                #me dan numeros aletorios entre -1 / 0 / 1
print(arr04)

print(np.multiply(arr01,arr01).sum())       #multiplica dos matrices y suma todos sus valores

