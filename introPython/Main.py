from modulo1 import *
####################################
#print("hola mundo")
#sNombre = input("como te llamas?")
#iNacimiento = int(input("en que año nacistes?"))
#edad = 23 - iNacimiento
#print(edad)
#print(f"te llamas {sNombre} y tienes {edad} años)
####################################

# fSalario = float(input("cual es tu salario mensual"))
# iAntiguedad = int(input("cuantos años llevas en la empresa"))
# fSaldo = float(int(input("cual es tu saldo en el banco")))
# bReportado = bool(int(input("estas reportado (1=si, 0=no)")))
# fValor = float(input("cuanto dinero necesesitas?"))
# darPrestamo = OtorgarPrestamo(fSalario, iAntiguedad, fSalario, bReportado, fValor)
# print(f"otrogar prestamo: {darPrestamo}")

#usando una funancion pura una lista de enteros:
#listaPrueba = [2, 4, 7, 3, 9]
# print("la lista de modificada po la funcion pura:")
# print(unaFuncionPura(listaDeEntrada(listaPrueba)))
# print("la lista original:")
# print(listaPrueba)

#una lista der cadena de caracteres
listaprueba2 = ["duvan", "andres", "rodiguez", "villalobos"]

# #una lista de elementos de varios tipos
# listaPrueba3 = [True, "duvan", 1.525, 58, listaPrueba]

# varPrueba = float(input("ingrese un valor numerico:"))
# tipoFuncion = input("que funcion deseas usar? 1. al cuadrado 2. al cubo")
# if tipoFuncion == "1":
#     funcionAUsar = pow2
# else:
#     funcionAUsar = pow3
        
# print("el resultado con la funcion elegida es:")
# print(funcionAUsar(varPrueba))    


# tipoFuncion = input("que deseas usar? 1. mayuscula 2. minuscula:")
# if tipoFuncion == "1":
#     funcionAUsar = convertirAMayusculas(listaprueba2)
# else:
#     funcionAUsar = convertirAMinusculas(listaprueba2)
    
# print("el resultado de la funcion elegida es:")
# print(funcionAUsar)


listaConvertir = list(map(mayus, listaprueba2))
print("lista a mayuscula")
print(listaConvertir)