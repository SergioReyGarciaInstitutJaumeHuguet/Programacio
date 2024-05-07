#algorisme que trobi la suma dels n primers nombres imparells.
num1 = 1
contador = 1
suma = []
x = 0
veces = int(input("¿Cuantos números impares quieres sumar? "))
while contador <= veces:
    num1 = int(input("¿Cual es el número impar? "))
    if num1 %2:
        contador +=1
        suma.append(num1)
    else:
        continue
x = sum(suma)
print("La suma total es ", x)