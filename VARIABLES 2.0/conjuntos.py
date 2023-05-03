#creando un conjunto con set()
conjunto = set(["Dato1"])
#metinedo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjungo2 = {conjunto1, "dato 3"}
print(conjungo2)


#Teoria de conjuntos, conjuntos y subconjuntos. 


conjunto_1 = {1,3,4,5,8}
conjunto_2 = {1,3,8}

resultado = conjunto_2.issubset(conjunto_1) # verifica si el conjunto dos, es un subconjunto de b, es decir, valida si los datos estan ingresados en el conjungo mayor
resultado = conjunto_2 <= conjunto_1 # esto devuelve la misma validación, ya que es validación de conjuntos, no va a validar si es mayor o menor
print(resultado)

resultado2 = conjunto_1.issuperset(conjunto_1)
print(resultado2)