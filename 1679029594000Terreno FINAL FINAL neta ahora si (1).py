import random

#Aquí podemos dimensionar nuestro terreno ren = renglones | col = columnas.
ren = 15
col = 30
#Aquí se empieza la generación del terreno y los obstaculos.
obstaculos = ['X','=']
terreno = []
aguatot = 0
obstot = 0
for i in range(ren):
    fila = []
    for j in range(col):
        fila.append(random.randint(0, 6))  #Ponemos que se generen numeros del 1 al 6 para sustituir el 6 con los obtaculos.
        for i in range(len(fila)):  # El 6 puede ser agua u obstaculo aleatoriamente con probabilidad de 50%
            if fila[i] == 6:
                fila[i] = obstaculos[random.randint(0,1)]  # si agregamos otro if podemos modificar la proporción de agua contra obstaculos
    agua = fila.count('=')
    aguatot += agua
    obs = fila.count('X')
    obstot += obs
    terreno.append(fila)

xnave = random.randint(0,col-1)
print(xnave)
ynave = random.randint(0,ren-1)
print(ynave)
terreno[ynave][xnave] = '*'  #Aquí se agrega la neve de manera aleatoria 

#Aquí se imprime el terreno con la condicion de que si hay más columnas que filas no se pueda correr.
#Tambien se genera la delimitacion del terreno y la información general de todo.

num_columnas = len(terreno[0])
for fila in terreno:
    if len(fila) != num_columnas:
        raise ValueError("El número de columnas en las filas no coincide")

if len(terreno) < col:
    terreno[+1].extend([0] * (col - len(terreno[-1])))

print('El agua esta representada por "=" y los obstaculos por "X"')
print(f"\n hay {aguatot} unidades de agua y {obstot} obstaculos. \n La nave está en {xnave}, {ynave} \n")

print("#" * (col+2)) 
for i in range(ren):
    print("#", end="")
    for j in range(col):
        print(terreno[i][j], end="")
    print("#") 
print("#" * (col+2)) 