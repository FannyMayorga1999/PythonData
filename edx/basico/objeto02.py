#devuelve una copia de la cadena con todos los caracteres en mayúsculas convertidos a minúsculas
x = "HOLA"
x= x.lower()
print(x)

#devuelva una copia de la cadena con su primer carácter en mayúscula y el resto en minúscula
y = "hola fanny"
y= y.capitalize()
print(y)

#devuelva una copia de la cadena con todos sus caracteres en mayusculas
z = "hola"
z = z.upper()
print(z)

a = 7
b = a
a = 3
print(a,", ",b)

#strip elimina un elemento selecionado dentro de un string 
stri = "*****this is string example....wow!!!*****"
print (stri.strip( '*' ))

palabra = 'que es eso? eso es queso '

#define los delites de los arreglos o de las variables 
print(palabra[0:11])
print(palabra[-13:-1])

 #me dice si la palabra, silaba o letra se encontra pero con un -1 o 0
print(palabra.find('que'))


#Convertir string a numbers

palabra01 = '1234'
print(int(palabra01))       #convierto a enteros
print(float(palabra01))     #convierto a enteros con decimales

#format es una funcion para arreglar elementos dentro de un array o string pero se debe definir espacios con corchetes para
#agregar otros string, al definir los corchete y no llenar los espacios nos salgar un error al interpretar
palabra02 = 'Nosotros amamos {} {} {}  . '
print(palabra02.format('la','vida', '<3' ))