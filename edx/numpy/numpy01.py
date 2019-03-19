#py -m pip install numpy installar numpy ((Instalador))
import numpy as np

"""Numpy es una libreria de python para operar matrices o vectores soporta array de multi dimensiones llamados ndarray """


#arrange define el rango de las matrices o el tamaño de la matriz
#el reshape define las columnas y las filas el primer numero define fila ! y segundo columnas --
a = np.arange(15).reshape(3, 5)
print(a)

b = np.arange(15).reshape(5,3)
#print(b)

c = np.array([3,33,333])    #definicion de matriz
print(type(c))              #que tipo de matriz es 
print(c.shape)              #tamaño de matriz


d = np.zeros((2,2))         #define un matriz nula
print(d)

e = np.full((2,2), 9)       #define un matriz un solo elemento igual
print(e)

f = np.eye(4,5)             #definir una matriz identidad 
print(f)

g = np.ones((4,4))          #definir una matriz de identidad 
print(g)

h = np.random.random((4,5)) #matriz aletoria con numeros decimales entre 0 - 1
print(h)