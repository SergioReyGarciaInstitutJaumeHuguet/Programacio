# Ejercicio 2

x = 1
a = 0
par = 0
impar = 0
sumpar = 0
sumimpar = 0
maxpar = 0
maximpar = 0
minpar = 891846549865189564
minimpar = 9845698654168541986546
max = 0
min = 0
while x != 0:
    x = int(input("Dime un número, si quieres finalizar pon 0: "))
    if x == 0:
        continue
    a = x % 2
    if a == 0:
        par += 1
        sumpar += x
        if maxpar < x:
            maxpar = x
        if minpar > x:
            minpar = x
    else:
        impar += 1
        sumimpar += x
        if maximpar < x:
            mamimpar = x
        if minimpar > x:
            minimpar = x
if minpar == 891846549865189564:
    minpar = 0
if minimpar == 9845698654168541986546:
    minimpar = 0
if maxpar > maximpar:
    max = maxpar
elif maximpar > maxpar:
    max = maximpar
if minpar < minimpar:
    min = minpar
elif minimpar < minpar:
    min = minimpar
print(f"Has introducido {par} números pares y {impar} números impares. La suma de los pares son {sumpar} y de los impares son {sumimpar}. El número mas grande que has introducido ha sido {max} y el más pequeño ha sido {min}.")
