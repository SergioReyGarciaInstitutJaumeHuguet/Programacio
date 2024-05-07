#Ejercicio 5

paraula = 1
letra = 0
corta = 5964198654
resto = 0
larga = 0
countcorta = 0
countlarga = 0
countantcorta = 5964198654
countantlarga = 0
palabracorta = ""
palabralarga = ""
y = ""
x = input("Dime una frase: ")
for i in x:
    letra += 1
    resto += 1
    if i == " ":
        resto -= 1
        paraula += 1
        if corta > resto:
            corta = resto
            for z in y:
                countcorta += 1
            if countcorta < countantcorta:
                palabracorta = y
        if larga < resto:
            larga = resto
            for z in y:
                countlarga += 1
            if countlarga > countantlarga:
                palabralarga = y
        resto = 0
    y += i
    if i == " ":
        y = ""
resta = letra - (paraula - 1)
print(f'El número de letras totales son {resta}, hay {paraula} palabras, la palabra mas corta "{palabracorta}" contiene {corta} letras y la mas larga "{palabralarga}" contiene {larga}')