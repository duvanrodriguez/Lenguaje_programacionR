# def OtorgarPrestamo( pSalario, pAntiguedad, pSaldoBancario, pGastosMensuales, pReporte, pValorSolic ):
#     if pSalario > 1200000.0 and pAntiguedad > 2 and pValorSolic <= pSaldoBancario and pReporte == False:
#         return True
#     else:
#         return False
    
#una funcion pura en python (no modifica el parametro de entrada, crea una
# nueva variable)
#entrada: una lista de enteros
#salida: una copia de la lista de entrada, con sus valores al cuadrado 
def unaFuncionPura(listaDeEntrada):
    #una lista vacia en python
    listaSalida = []
    #iterando en una lista
    for x in listaDeEntrada:
        #agregando un elemento a un lista
        listaSalida.append(x**2)
        
    return listaSalida

def pow2(var):
    return var**2

def pow3(var):
    return var**3

def convertirAMayusculas(listaEntrada):
    listaNueva = []
    for nombre in listaEntrada:
        listaNueva.append(str(nombre).upper())
    return listaNueva

def convertirAMinusculas(listaEntrada):
    listtaNueva = []
    for nombre in listaEntrada:
        listtaNueva.append(str(nombre).lower())
    return listtaNueva

def mayus(item):
    return(str(item).upper())