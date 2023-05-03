#creando una funcion que nos devuelva los numeros primos
#entre el 0 y el numero que psamos


#creamos una funcion que verifica si un numero es primo
def es_primo(num):
    #verificamos qu ele numero pasado no pueda dividirse entre dos
    for i in range(2,num-1):
        #si es divisilble por algun numero entonces retormanos false
        if num%i==0: return False
    return True


#creando una funcion que
def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True:primos.append(i)
    return primos

resultado = primos_hasta(25)
print(resultado)