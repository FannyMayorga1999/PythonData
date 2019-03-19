#def para declarar funciones

#_init_ declara al objeto 

#self declarar los atributos del objeto

name= str(input("ingresa tu nombre"))
age= int(input("Ingresa tu edad"))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

people = Person(name, age)

print("Hola ",people.name, "tu edada es ", people.age)

