animales = ["pez", "gat", "perro", "loro", "cocodrilo"]
numeros = [34, 54, 6, 7, 72]

for animal in animales:
    print(animal)

#for anidados 

#iterando al mismo tiempo dos listas, deben ser del mismo tamaño las listas. 
for numero, animal in zip(numeros, animales):
    print(f"recorriendo lista 1: {numero}" )
    print(f"recorriendo lista 2: {animal}" )
    
for numero in range(5, 10):
    print(numero)
    
    
    #forma correcta de recorrer lista  por su indice

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice e: {indice} y el valor es: {valor}')
    
    
#usando el else

for numero in numeros:
 print(f"ejecutando el ultimo bucl, valor actual: {numero}")
else:
    print("el blucle finalizo")