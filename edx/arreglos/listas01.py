lista = [11,22,33]

#cambio de variables en un lista
lista[1] = 55


#eleminar un elemnto dentro una lista especificando el la posicion del elemnto de la lista
lista.pop()

#eleminar un elemnto dentro una lista especificando el elemnto de la lista
lista.remove(55)

#agregar un elemnto a la listas 
lista.append(22)
lista.append(33)

lista02 = [44,55,66]

#agrega otra lista 
lista.extend(lista02)

#agrega otra lista dentro de otra
lista.append(lista02)

for i in lista:
    print (i)

#or 
#itera dentro de las listas de columnas
for x,y in zip(lista,lista02):
    print(x,',',y)

"""for j in range(0,len(lista)):
    print(lista[j])"""



