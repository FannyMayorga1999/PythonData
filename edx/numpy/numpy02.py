import numpy as np

a = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]])
#print(a)

#index para saber desde comenzar a leer el la matriz hasta donde terminarla
b = a[:3, 1:3]
#print(b)



#CONDICIONES DE LAS MATRICES

b = np.arange(35).reshape(7, 5)
c = [(b >= 10) & (b <=22 )]             # & and -- | or
d=[(b % 2 == 0)]                        # modo
#print(d)


# TIPOS DE NDARRYS 

matriz01 = np.array([10,11,12,14,15])   #tipo de variable dentro de la matriz dtype
print(matriz01.dtype)

matriz02 = np.array([10.2,11.4,12.45,14,15])   #tipo de variable dentro de la matriz dtype
print(matriz02.dtype)

matriz03 = np.array([20,21,22,23,24], dtype = np.float64)  #cambio de tipo de variables
print(matriz03)

x = np.array([1, 2, 2.5]).copy() #copiar en la memoria 
print("hola",x)


#OPERACIONES CON NDARRAYS
sumaMatriz = matriz03 + matriz02        #suma de matrices
#print(sumaMatriz)
print(np.add(matriz03,matriz02))

restaMatriz = matriz03 - matriz02       #resta de matrices
#print(restaMatriz)
print(np.subtract(matriz03,matriz02))

multiMatriz = matriz03 * matriz02       #multiplicacion de matrices          
#print(multiMatriz)
print(np.multiply(matriz03,matriz02))

diviMatriz = matriz03 / matriz02        #division de matrices
#print(diviMatriz) #or 
print(np.divide(matriz03, matriz02))

sqrtMatriz = (np.sqrt(matriz01))        #calcula la raiz de matrices
print(sqrtMatriz)

print(np.exp(matriz01))                 #eleva la matrices por si misma 

