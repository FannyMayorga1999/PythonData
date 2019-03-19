#py -m pip install -U matplotlib (Instalador)
import matplotlib.pyplot as plt
import numpy as np
   

imagen =  plt.imread("C:/Users/admin/Documents/Fanny Mayorga/Capturas/imagen01.jpg") #lee la data de la imagen

datosFoto = np.array(imagen)    #defines la data a una ndarray

datosFoto[200:300, :,  2]= 10

datosFoto[400:500, :,  1]= 50

datosFoto[550:650, :,  0]= 250

datosFoto[0:100, :,  -1]= 250   #define de a donde va ser modificado y color que va tener entr e 0 / 255

imagen = plt.figure(figsize=(5,5))       #tamaño de la imagen 

#print(datosFoto.shape)         #nos enseña el tamaño de ndarray

#print(datosFoto)

#plt.imshow(datosFoto) 

#plt.show()


#c = np.add(datosFoto,datosFoto)

#SACAMOS UN CIRCUNFERENCIA PARA DEFINIR LA FORMA DE LA IMAGEN

totalFilas, totalColumnas , totalCapas = datosFoto.shape            #definimos para las dimensiones de ndarray una variable

X , Y = np.ogrid[:totalFilas, :totalColumnas]                       #definimos desde a donde vamos a poner las posiciones            

centroFilas , centroColumnas = totalFilas / 2 , totalColumnas / 2   #encontramos el centro del circulo

distCentro = (X - centroFilas)**2 + (Y - centroColumnas)**2         #definimos las circuferencias

radio = (totalFilas/2)**2                                           #calculamos el radio

circuloMascara = (distCentro < radio)                               #dibujo de la circuferencias donde si nos da false no se 
                                                                    #mostrara la imagen y si es true lo contrario

#datosFoto[circuloMascara] = 0                                      #para pintar la parte que nos da false o decir lo que esta 
                                                                    #fuera de la circuferncias

mediaMáscara = X < centroFilas
mediaMáscaraSuperior = np.logical_and(mediaMáscara, circuloMascara)

#datosFoto[mediaMáscaraSuperior] = 255                                          

plt.imshow(datosFoto)


plt.show()

print(datosFoto.shape)           #tamaño de data

"""----------------------------------------------------------------------------------------------------------------------"""
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




