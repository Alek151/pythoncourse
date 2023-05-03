import pandas as pd
df = pd.read_csv("archivo_prueba_csv.csv")
df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))
df["nombre"].replace("Alexander", "maestro")
#elimina filas con datos faltates
df_null = df.dropna()
print(df_null)
#eliminar filas repetida
df = df.drop_duplicates()
print(df)
#creando un csv con el dataframe resultante
df.to_csv("csv_datos_limpios.csv")