#Metodos para listas y poder operarlas
# LIST crea una lista
Lista = list(["hola", "componente", 34])
print(Lista)
cantidad_lementos = len(Lista)
#agregando un elemento nuevo a la lista
Lista.append("Vistador") # pasamos el valor que deseemos agregar
print(Lista)
#INSERT agregando elemento en indice específico
Lista.insert(2, "verificando") # pasamos como primer parametro la posición donde se agregará el segundo elemento.
print(Lista)
#extend agrega varios elementos a la lsita
Lista.extend([False, True, 23, 45]) # Se agregan elementos a partir de la ultima posición es otra lista completa la que podemos agregar
print(Lista)
#eliminado elementos de la lista (por indice)
Lista.pop(0) #eliminamos un elemnto que esté en su posición 0
Lista.pop(-1) #esto para eliminar el último elemento de una lista
Lista.pop(-2) # para eliminar el primero de la lista
print(Lista)
#removiendo un elemnto de la lista por su valor
Lista.remove("componente") # si encuentra un parametro que se encuentra en la lista, lo elimina, si no lo tiene, lanza una excepcion
print(Lista)
#Clear
Lista.clear() # elimina todo los elementos.
numerico = [1,4,5,6,5,343,4,454]
#ordenamiento de lista.
numerico.sort() #ordena del menor al mayor
numerico.sort(reverse=True) # los ordena del mayor al menor
print(numerico)

Lista.reverse() #esto solo invierte la lista como este escrita.
print(numerico)
