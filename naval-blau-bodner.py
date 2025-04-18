from typing import List  # priemro habimso puesto list src sin importar nada y despues le preguntamso a chat y nos dijo q importemos esto porque python por si solo no lo tenia 


n: int = 10
l: List[List[str]] = []  # El tablero: una lista de listas de strings

for i in range(n):
    fila: List[str] = [" "] * n
    l += [fila]

    # aca tuviuuumos un tema que queriamos un
    #a cuadricula y pensamos que printenado una por una lo ibamos a resolver (

for fila in l:
    print(fila)

l[1][5] = "x"
l[0][5] = "x"

barcos: List[str] = ["1,5", "0,5", "4,6", "5,5"]

aciertos: int = 0

for i in range(3):
    disparo: str = input("Ingresa un disparo (formato fila,columna): ")
    if disparo in barcos:
        print("¡Le pegaste!")
        aciertos += 1
        barcos.remove(disparo)

        # buscamos como eliminaf un elemento
    else:
        print("Fallaste")

print("Aciertos:", aciertos)
print("Fallos:", 3 - aciertos)
print("Tablero final:")
for fila in l:
    print(fila)
