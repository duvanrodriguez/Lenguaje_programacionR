from LoadData import *

def filtroAves(humedal):
    return humedal["aves"] > 30

nombreArchivo = input("que archivo vamos a leer?")
miDataSe = LoadData(nombreArchivo)
print(miDataSe)

dataSetFiltrado = list(filter(filtroAves, miDataSe))
print(dataSetFiltrado)

#filtrar humedales con especies de aves mayores a 30


# LoadData(nombreArchivo)
# print(miDataSet)

# #tipo de diccionario para la informacion de un humedal
humedal1 = {"nombre": "lago de las garzas",
            "direccion": "calle 43 54",
            "hectarias":4.7,
            "especies de aves":149,
            "especies de floras":148,
            "estado": "en conservacion"}
print(humedal1["nombre"]) 