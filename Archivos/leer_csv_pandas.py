import pandas as pd
archivo = pd.read_csv("Archivos\\archivo_prueba_csv.csv")
archivo2 = pd.read_csv("Archivos\\archivo_prueba_csv.csv")
nombres = archivo["nombre"]
print(nombres)
#ordenando el dataframe por la edad
df_ordenado = archivo.sort_values("edad")
#ordenandolo de forma desedencete
df_ordenado_ascendente = archivo.sort_values("edad", ascending=False)
#mostramos en consola los datos
print(df_ordenado_ascendente)
#concatenando dos dataframes
df_concatenado = pd.concat([archivo, archivo2])
print(df_concatenado)
#accediendo a la primer fila con head8
primer_fila = archivo.head(1) #dentro de parentesis mostramos las filas que quermos mostrar
#accediendo a la ultima fila
ultima_fila = archivo.tail(3)
print(primer_fila)
print(ultima_fila)
#accendientdo a la cantidad de filas y columas con shap
filas_y_columnas = archivo.shape
#obteniendo datos estadistica del dataframe;
df_info = archivo.describe()
print(df_info)
#accedidneod a un elemento especifico del dr con loc
elemento_especifico = archivo.loc[2, "edad"]
#accedidneod a la edad de la fila 2 con iloc
elemento_especifico2 = archivo.iloc[2,2]
#accendiendo a todas las filas de una columna
apellidos = archivo.loc[:, "apellido"]
#accdiendo a la fila 3 con loc
fila_3 = archivo.loc[2,:]
print(fila_3)
#Accndiendo a filas con edad mayuor que 30
mayor_que_30 = archivo.loc[archivo["edad"]>30,:]
print(mayor_que_30)

