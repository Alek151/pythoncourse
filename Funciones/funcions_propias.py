#creando una funcion suimple
def saludar():
    print("Hola Alex, como estas")
#ejecutando la función simple
saludar()
#creando una función con parametro
def saludar2(nombre):
    print(f"hola como estas {nombre}")
saludar2("Alexander")
#creando una función que no retorne valores
def crear_contraseña_random(num):
    chars = ["abcdefghij"]
    num_entero = str(num)
    c1 = num_entero - 2
    c2 = num_entero
    c3 = num_entero - 5
    contrasña = f"bienvendos"
    return contrasña
#retorna el valor y lo podemos ejecutar variables diferentes. 
