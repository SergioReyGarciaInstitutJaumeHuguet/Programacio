#Si tenim una cadena amb un nom i cognoms, realitzar un programa que mostri les inicials en majúscules.
frase = input("Dime una frase sin mayusculas: ")
inicio = True
iniciales = ""
for i in frase:
    if inicio == True:
        iniciales += i.upper()
        inicio = False
    if i == ' ':
        inicio = True
print(iniciales)