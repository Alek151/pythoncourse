def sumar_2():
    while True:
        a = input("Numero 1: ")
        b = input("numero 2: ")
        try: 
           resultado = int(a) + int(b)
        except:
            print("El valor ingresado no es númerico")
        else:
            break
    return resultado

print(sumar_2())