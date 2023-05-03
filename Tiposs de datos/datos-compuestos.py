#datos comuestos
lista = ["Alex Garcia", "Soy Developer", True, 1.68]
#Imprimir toda la lista
print(lista)
#Imprimir un valor de la lista
print(lista[2])
#Recordando que iniciamos a programar desde 0, ya que es el número inicial 
#cambiando el valor de un dato en la lista
lista[1] = "Alexander" # Dato ha sido moficado
print(lista)
#TUPLAS
# las desventajas de usar tuplas, es que no se pueden modificar, las listas sí lo permiten, los datos integrados en la tupla, nunca podrán ser modificados. 
tupla = ("Briayan Garcia", "Soy Analista", False, 1.69)
print(tupla)
#Conjunto 
#se puede modificar la posición de los elementos, más no modificar su valor. 
conjunto = {"Briayan Garcia", "Soy Analista", False, 1.69}
#el conjunto puede reconstruirse. No se muestra la repetición de valores duplicados. 
#no podemos acceder como accesamos en una lista. 
#diccionario
#make a dict

diccionario = {
     'nombre': "Alexander Garcia",
     'Puesto': "Analista Programador",
     'altura': 1.87
}
#imprimiendo el diccionario
print(diccionario)
#accediendo a un valor en especifico
print(diccionario['nombre']) #no se accede por sus indices, si no por su valor en el diccionario. 

