edad = 17

#tomar muy en cuenta la identación en Pyton, ya que no funciona igual que en otros lenguajes
#la identación debe estar correcta, ya que si se agrega otra trabulación, el programa dejará de funcionar.

if edad >= 18: #evaluamos la condicion
    print("Es mayor, podes pasar") # realizamos la acción si se cumple
else: #Si no se cumple la condición deseada
  print("No es mayor, no puedes pasar") #accion al no cumplirse
  
print("Prigrama finalizado")


contrasena_almacenada = "DaltoMestro"
contrasena_escrita = '''DaltoMestro'''

if contrasena_almacenada == contrasena_escrita:
    print("Bienvenido")
else: 
    print("Contraseña incorrecta")