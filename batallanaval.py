n = 10
l = []
for i in range(n):
    fila = [" "] * n
    l += [fila]

    # aca tuviuuumos un tema que queriamos un
    #a cuadricula y pensamos que printenado una por una lo ibamos a resolver (
for fila in l:
    print(fila)
l[1][5] = "x"
l[0][5] = "x"
barcos = ["1,5", "0,5", "4,6" , "5,5"]

aciertos = 0

for i in range(3):
    disparo = input("Ingresa un disparo (formato fila,columna): ")
    if disparo in barcos:
        print("¡Le pegaste!")
        aciertos += 1
        barcos.remove(disparo)
        #buscamos como remover un elemento
    else:
        print("Fallaste")

print("Aciertos:", aciertos)
print("Fallos:", 3 - aciertos)
print("Tablero final:")
for fila in l:
    print(fila)

