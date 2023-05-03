multiplicar_por_dos = lambda x : x * 2
print(multiplicar_por_dos(3))
#creando una funcion lambda para multiplicar por dos
#creando una funcion comun que diga si es par o no
numeros = [1,2,3,4,5,6,7,8,9]
def es_par(num):
    if(num%2==0):
        return True
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))
#creando lo anterior con lambda
numeros_pares2 = list(filter(lambda numero:numero%2 == 0, numeros))
print(numeros_pares2)