ingreso_mensual = 100000
gasto_mensual = 7000

#condicion else if (elif) hace una comparación extra si la primera no sé cumplió
#if anidadados


if ingreso_mensual > 10000:
    if gasto_mensual < ingreso_mensual: # podemos colocar condiconales adicionales dentro de cada if,  y a esto otro elif si lo deseamos
        print("Estas bien economicamente")
    if gasto_mensual > ingreso_mensual:
        print("No te alcanza")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
else:
    print("no hay money")
    
print("fin del programa")