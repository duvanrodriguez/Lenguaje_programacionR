from LoadData import *

#funcion 
def filtroAves(humedal):
    return humedal["aves"] > 100

nombreArchivo = input("que archivo vamos a leer?")
miDataSe = LoadData(nombreArchivo)
print(miDataSe)

#filtra humedales con especies de aves mayores a 30(con una funcion ya definida)
dataSetFiltrado = list(filter(filtroAves, miDataSe))

#uso de filtro con una funcion anonima
#lambda significa funcion anonima, x: seria el parametro, x lo que retorna
dataSetFiltrado2 = list(filter(lambda x:x["hectarias"]>4.0 , miDataSe))
print(f"Humedales filtrados {len(dataSetFiltrado)} \n")
print("humedal filtrado 1 (aves:)")
print(dataSetFiltrado)
print("humedales filtrado 2 (hectarias)")
print(dataSetFiltrado2)

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