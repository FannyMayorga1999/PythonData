#TUPLES es un tipo de lista que no se puede cambiar 
tuple01 = ['hola','bola','joven','XD']
print(tuple01)

#DICIONARIOS es un tipo de lista que tiene llave con valor
persona= {
    "nombre": "Fanny",
    "apellido":"Mayorga",
    "edads" : 19
}
print(persona)

#Un conjunto es una colección desordenada de elementos. Cada 
#elemento es único (sin duplicados) y debe ser inmutable (que no se puede cambiar).
#Sin embargo, el conjunto en sí es mutable

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)


#Discord sirve para desavilitar un elemnto de los arreglos

numbers = {2, 3, 4, 5}

numbers.discard(3)
print('numbers = ', numbers)

numbers.discard(10)
print('numbers = ', numbers)