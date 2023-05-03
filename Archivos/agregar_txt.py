with open("archivo_texto.txt", "a", encoding="UTF-8") as archivo:
     archivo.write("\n")
     for i in range(5):
        archivo.write(f"linea {i+1} agregada")