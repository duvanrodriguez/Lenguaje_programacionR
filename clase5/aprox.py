from functools import reduce

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_term(i):
    return 1 / factorial(i)

def approximate_e(N):
    terms = map(calculate_term, range(N))
    approximation = reduce(lambda x, y: x + y, terms)
    return approximation

# Solicitar al usuario la cantidad de términos para la aproximación
N = int(input("Ingrese la cantidad de términos para la aproximación de e: "))

if N >= 0:
    result = approximate_e(N)
    print(f"Aproximación de e con {N} términos: {result}")
else:
    print("El número de términos debe ser mayor o igual a 0.")