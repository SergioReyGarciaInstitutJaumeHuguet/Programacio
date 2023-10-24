#Algorisme que compti el nombre de "LA" dins una seqüència de caràcters.
print("Dime una frase")
x = input("")
z = 0
y = 0
h = 0
for i in range(len(x)):
    caracter = x[i]
    if caracter == "L" or caracter == "l":
        h += 1
    if caracter == "a" or caracter == "A" and h == 1:
            h = 0
            y += 1
    else:
         h = 0
print(f"Las veces que sale 'la' en la frase son: {y} veces")