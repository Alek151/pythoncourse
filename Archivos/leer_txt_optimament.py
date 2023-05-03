#abriendo ael archivo con with open
with open("archivo_texto.txt") as archivo:
    contenido = archivo.read()
    print(archivo.read())
    
    #con esto logramos el archivo ejecutar un comando, al terminar lo que indiquemos el arvchivo se cierra automáticamente. 
    
