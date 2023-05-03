archivo = open("archivo_texto.txt", encoding="UTF-8")
#print(archivo.read())
lineas = archivo.readlines()
print(lineas)
#cerramos el archivo
archivo.close()
archivo_leido = archivo.read()

