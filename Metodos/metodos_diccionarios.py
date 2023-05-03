#Trabajando con diccionarios

diccionario = {
     'nombre': 'Alex',
     'apellido': 'Garcia',
     'subs': 9
}
claves = diccionario.keys() #muestra todas las llaves de datos que existen en el diccioinario
print(claves)
obtener = diccionario.get('nombre') #muestra el valor de la llave ingresada / esto me ayuda a no mostrar errores si el Key no se encuentra
print(obtener)

#eliminando un elemento del diccionario
diccionario.pop('nombre') # eliminamos la key
print(diccionario)

#obteniendo un elemento de dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
#clear elimina todo los elementos del diciconario
diccionario.clear() #vacia los datos
print(diccionario)
