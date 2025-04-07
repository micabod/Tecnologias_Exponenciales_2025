n = 10
l = []
for i in range(n):
    fila = [" "] * n
    l += [fila]

for fila in l:
    print(fila)
l[1][5] = "x"
l[0][5] = "x"



barcos = ["1,5", "0,5"]

disparo = input("Ingresa un disparo (formato fila,columna): ")

if disparo in barcos:
    print("¡Ganaste!")
else:
    print("Fallaste")

    # aca tuviuuumos un tema que queriamos una cuadricula y pensamos que printenado una por una lo ibamos a resolver (

#input ("ingresa un disparo")
# nostroas mediante el codigo poner los barcos ponele (o;1). despues el usuario con el disparo ver si le pego as un bargo o no le pego 
# si no le ga poner un mensaje y si le page gano otro mensaje
# Ponemos barcos (marcamos con "x")