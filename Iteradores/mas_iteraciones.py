frutas = ["banana", "naranja", "ciruela", "pera", "durazno"]

for fruta in frutas:
    if fruta == "franada":
        continue
    print(f"me voy a comer una {fruta}")
    
    
#recorrer una cadena de texto
cadena = "Hola como estas"

for letra in cadena:
    print(letra)
   
numeros = [1,4,5,6,8]
    
#for en una sola lina de código
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numeros*2)
numeros_dupliocados_2 = [x/2 for x in numeros]  
print(numeros_dupliocados_2)