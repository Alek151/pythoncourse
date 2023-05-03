#tenemos dos listas con nombre y apellido 

nombres = ["Lucas", "Alexander", "Jorge", "Arturo"]
apellidos = ["Dalto", "Garcia", "Montolla", "Caceres"]

#resgistrar esata información en un TXT de forma rapido

with open("Nombres_Apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n")
    [arch.writelines(f"Nombre: {n}\n Apellido: {a}\n ") for n,a in zip(nombres,apellidos)]
