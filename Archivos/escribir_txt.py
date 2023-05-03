with open("archivo_texto.txt", "w", encoding="UTF-8") as archivo:
    #sobre escribiendo el archivo
    archivo.write("jajaj ya escrbiste un texto jaja")
    #escribe lineas en el archivo enviadas por medio de un array
    archivo.writelines(["Hola Capo", "Bienvenido"])
    