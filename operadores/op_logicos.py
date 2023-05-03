#AND 
#ando se cumplen si ambas son verdaderos

resultado = True & True #Devuelve verdadereo
resultado = False & True #Devuelve falso
resultado = True & False #Devuelve falso
resultado = False & False #Devuelve falso


#OR compara otro valor
#Devuelve verdadero si al menos una es verdadera

resultado = True | True #Devuelve verdadereo
resultado = False | True #Devuelve verdadero
resultado = True | False #Devuelve verdadero
resultado = False | False #Devuelve falso

#NOT 
#intercambia el resultado del valor, si es verdadero pasa a ser falso. 
resultadoNot = not 2 > 49 #Devuelve True
resultadoYes = not 2 < 49 #Devuelve verdadero
print(resultadoNot)
print(resultadoYes)