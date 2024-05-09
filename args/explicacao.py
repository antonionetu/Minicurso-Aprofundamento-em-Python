# Sem usar args
def soma_dois_numeros(a, b):
    return a + b

def soma_tres_numeros(a, b, c):
    return a + b + c

def soma_quatro_numeros(a, b, c, d):
    return a + b + c + d


# Usando args
def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(soma(1, 2, 3, 4))