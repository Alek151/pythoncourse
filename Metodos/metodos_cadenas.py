cadena_1 = "Hola soy Alexander"
cadena_2 = "Bienvenido Crack"
#dir nos dice que podemos hacer con el tipo de dato que tengamos, tomando en cuenta los tipos de datos existentes. 
## print(dir(cadena_1))
#Funciones de transformación de datos
resultado = cadena_1.upper() #convirte todo el texto a mayusculas
resultado = cadena_1.lower() #convierte el texto a minusculas
resultado = cadena_1.capitalize() # Convertimos la primera letra en mayuscula y las letras siguientes las coloca en minuscula.
print(resultado) 
#Metodos de buqueda
busqueda = cadena_1.find("3") #Devolvera la posición en la que encontró la primera letra
#Si el resultado que imprime es -1 significa que la palabra o el valor no se encuentra dentro de la cadena.
print(busqueda)
busqueda_index = cadena_1.index("a") # esta funciona si no encuentra nada nos devuelve un error, una excepcion.
#Punto para ver, el manejo de errores
#metodos para consulta. 
# inumeric, si es numerico devuelve true, y si no devuelve false
validacion = cadena_1.isnumeric() # valida si es numerico solo numeros
validacion = cadena_1.isalpha() # valida si es alfanumerico numneros y letras
print(validacion)
#coincidencias y tamaño
#devuelve la cantidad de veces que se encuentra un dato en una cadena
conteo = cadena_1.count("a") # contará la cantidad de veces que a se encuentra en está cadena de texto
print(conteo)
conteo2 = cadena_1.__len__()  # esto hace lo mismo que lo de abajo, pero se mira más simple y ordenado.
conteo2 = len(cadena_1)
print(conteo2)

#Verifica si una caena empieza con otra cadena dada

validar = cadena_1.startswith("H") # le preguntamos si la cadena comienza con el valor que le indicamos
#de cumpñlirse devuelve True, y si devuelve False
validar = cadena_1.endswith("H") # esto cumple la misma funcionalidad, únicamente que esto valida el final de la cadena

#Reemplazo de valores

remplazar_datos = cadena_1.replace("a","b") # en este condigo reemplazamos todas las a por el segundo valor
#esto nos sirve para remplazar errores que vengan en la base de datos, o bien un CSV o datos ingresados incorrectos
print(remplazar_datos)

cadena_separada = cadena_1.split(" ") #separa la cadena, por el valor que le pasamos, pueden ser cualquier dato o letras
print(cadena_separada)
