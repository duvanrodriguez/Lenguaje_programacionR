from functools import reduce
from LoadData import *

#ejercicio: map y filter
#1. definir una funcion map para convertir el campo nombre de cada estado a miniscula
#2. aplicar con map
#3. definir una funcion filter para filtrar humedales con estados "en recuperacion"
#4. aplicar filter

#solucion
#1. definir funcion map para convertir el campo nombre de cada estado a minuscula

#2. aplicar con map
# def minusculas(r):
#     return { r["nombre"],
#                 r["hectarias"],
#                 r["aves"],
#                 r["flora"],
#                 r["estado"].lower()}


# #3. definir una funcion filter para filtrar humedales con estados "en recuperacion"

# #4. aplicar filtro

# def filtroEstado(humedal):
#     return humedal["estado"] == "en conservacion"

# nombreArchivo = input("que archivo vamos a leer? \n")
# miDataSe = LoadData(nombreArchivo)
# print(miDataSe)

# dataSetFiltrado = list(filter(filtroEstado, miDataSe))
# print("humedal en estado conservacion: \n")
# print(dataSetFiltrado)


# registro = {"nombre":"PAMPALINDA",
#             "direccion":"Calle 5a 62-00",
#             "hectarias":20.0,
#             "aves":54,
#             "flora":37,
#             "estado":"En conservación"}
# campo_mayus = registro["nombre"].lower()
#print("campo nombre a minuscula:")
#print(campo_mayus)

# miDataSe2 = list(map(minusculas, miDataSe))
# print("estado a minuscula: \n")
# print(miDataSe2)


#funcion reduce:
# def  Misuma(a,b):
#     return a+b
    
# listaNumerosPares = list(range(1,101,))
# print("numeros pares")
# print(listaNumerosPares)
# suma = 0
# #seri sumatoria, usando un iterador
# for i in listaNumerosPares:
#     suma = suma + i
# print(suma)

# listaCadena = ["Muchos", "años", "despues", ",", "frente", "al", "peloton"]


#serie sumatoria, usando la funcion reduce
#sumaTotalReduce = reduce(Misuma, listaNumerosPares)
# sumaTotalReduce = reduce(lambda x,y: x+y, listaNumerosPares)
# productoTotalReduce = reduce(lambda x,y: x*y , listaNumerosPares)
# inicioCienAnioSoledad = reduce(lambda x,y: x+" "+y, listaCadena)
# print(f"suma con reduce:{sumaTotalReduce}")
# print(f"producto con reduce:{productoTotalReduce}")
# print(f"cadena concatenada:{inicioCienAnioSoledad}")

def convertirAnios(x):
    return {
        x["nombre"],
        x["Edad"]/12,
        x["Edad"]
    }

def filtrarVegetarianos(x):
    x["Vegetariano"] == True

listaEstudiantes = [
    {"nombre":"Duvan", "Edad":552, "Vegetariano":False},
    {"nombre":"ANDRES", "Edad":24, "Vegetariano":False},
    {"nombre":"alejandra", "Edad":27, "Vegetariano":True}]

listtaEdadAnios = list(map(convertirAnios, listaEstudiantes))
print(f"map:{listtaEdadAnios}")

listaVegetarianos = list(filter(lambda x:x["Vegetariano"]==True,listaEstudiantes))
listtaEdadAnios = list(map(convertirAnios, listaVegetarianos))
print(f"filtro vegetariono:{listtaEdadAnios}")

# listaDatos = reduce(lambda x,y: x["nombre"]+"," y["nombre"], listaEstudiantes)
# print(f"cadena estudiante:{listaDatos}")
# listaNumeros = list(range(1,100,1))
# print("numeros")
# print(listaNumeros)

