import csv
with open("archivo_prueba_csv.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

#para trabajar con archivos muy grandes se rcomienda

#def read_csv_in_chuncks(file_name):
 #   for i, chunk in enumerate(pd.read_csv(file_name, chunksice=1000)):
 #       print("chunk #{}".format(i))
#        print(chunk)
#        
#read_csv_in_chuncks("big_fiule.csv")