import re
texto = "Hola pedro, mi numero es +54 77 6435-654654"

pattern= r'\+\d{2}\s\d{2\s\d{4}\d'

remplazo = re.sub(pattern, "Numero oculto", texto)

print(remplazo)