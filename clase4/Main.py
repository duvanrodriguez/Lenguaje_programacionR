from LoadData import *

#ejercicio: map y filter
#1. definir una funcion map para convertir el campo nombre de cada estado a miniscula
#2. aplicar con map
#3. definir una funcion filter para filtrar humedales con estados "en recuperacion"
#4. aplicar filter

#solucion
#1. definir funcion map para convertir el campo nombre de cada estado a minuscula

#2. aplicar con map
def minusculas(r):
    return { r["nombre"],
                r["hectarias"],
                r["aves"],
                r["flora"],
                r["estado"].lower()}


#3. definir una funcion filter para filtrar humedales con estados "en recuperacion"

#4. aplicar filtro

def filtroEstado(humedal):
    return humedal["estado"] == "en conservacion"

nombreArchivo = input("que archivo vamos a leer? \n")
miDataSe = LoadData(nombreArchivo)
print(miDataSe)

dataSetFiltrado = list(filter(filtroEstado, miDataSe))
print("humedal en estado conservacion: \n")
print(dataSetFiltrado)


registro = {"nombre":"PAMPALINDA",
            "direccion":"Calle 5a 62-00",
            "hectarias":20.0,
            "aves":54,
            "flora":37,
            "estado":"En conservación"}
campo_mayus = registro["nombre"].lower()
print("campo nombre a minuscula:")
print(campo_mayus)

# miDataSe2 = list(map(minusculas, miDataSe))
# print("estado a minuscula: \n")
# print(miDataSe2)


