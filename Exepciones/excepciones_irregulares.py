import re
texto = '''Hola maestro esta es la cadena 1
esta es la cadena de texto 2
y esta es la cadena de texto 3'''

#haciendo una busqueda simpñe
resultado = re.findall("esta", texto)

#\d -> busca digitos numeroc sdel 0 al 9
resultado2 = re.findall(r"\d", texto)

#\D busca Todo menos digitnos numerocos del 0 al 9

resultado3 = re.findall(r"\D", texto)

print(resultado + resultado2 + resultado3)