diccionario = {
    "nombre": "Alexander",
    "Apellido": "Garcia",
    "edad": 22 
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(key, value)