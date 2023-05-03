frase = input("Decime una frase y te digo cuanto tardas en decirla.")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/4} segundos en decirlo')

