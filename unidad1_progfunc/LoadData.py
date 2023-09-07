#Funciones para crear un dataset como una lista de tuplas
#a partir de un achivo plana
#param: la ruta del archiovo plano
def LoadData(fileName):
    dataset = []
    with open(fileName) as f:
        for line in f: #iterar x cada renglon del archivo
            values = line.split(sep=';') #funcion slpit: le estamos indicando que el separador es ;
            print(values)
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectarias":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            dataset.append(registro)
    return dataset