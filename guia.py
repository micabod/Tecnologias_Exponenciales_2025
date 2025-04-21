# ej uno

numeros = [1,2,3,4,5,6]

def obtener_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

resultado = obtener_pares(numeros)
print(resultado)

# ej 2
numeros = [1, 2, 3, 4, 5, 6]

def numero_grande(lista):
    if not lista:
        return 0  # si la lista está vacía
    grande = lista[0]  # empezamos suponiendo que el primero es el más grande
    for numero in lista:
        if numero > grande:
            grande = numero
    return grande

result = numero_grande(numeros)
print(result)

# ej 3
numeros = [1, 2, 3, 4, 5, 6]

def numero_chico(lista):
    if not lista:
        return 0  # si la lista está vacía
    chico = lista[0]  # empezamos suponiendo que el primero es el más grande
    for numero in lista:
        if numero < chico:
            chico = numero
    return chico

result = numero_chico(numeros)
print(result)
