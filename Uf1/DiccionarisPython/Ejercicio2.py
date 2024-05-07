# 2. Escriu un programa que llegeixi una cadena i retorni un diccionari amb la 
# quantitat d'aparicions de cada caràcter en la cadena.
dicc = {}
cadena = input("Dime una frase: ")
for caracter in cadena:
    if caracter in dicc:
        dicc[caracter] += 1
    else:
        dicc[caracter] = 1
for i, j in dicc.items():
    print(i + ': ' + str(j))

