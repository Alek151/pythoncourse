#falto el profesor y los alumnos daran la clase
#pedir el nombre y la edad de los compañeros que vinieron a dar la clase
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese tu edad"))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañero[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor
asistente, profesor = obtener_compañeros(2)
print(f"el profesor es_ {profesor}  y su asistente es {asistente}")