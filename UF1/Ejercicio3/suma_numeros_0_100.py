#Algorisme que sumi tots els números parells compresos entre 2 i 100.
num1 = 1
contador = 1
suma = []
x = 0
veces = int(input("¿Cuantos números pares quieres sumar? "))
while contador <= veces:
    num1 = int(input("¿Cual es el número impar? "))
    if num1 %0 and num1 <= 100 and num1 > 1:
        contador +=1
        suma.append(num1)
    else:
        continue
x = sum(suma)
print("La suma total es ", x)