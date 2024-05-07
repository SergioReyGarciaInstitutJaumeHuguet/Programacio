#Fer un programa per què et calculi el percentatge d'aprovats en una  
#assignatura  d'un vector on  hi ha emmagatzemades les notes dels alumnes de la classe. 
#El vector s'anirà omplint per teclat fins que el programa trobi un input sense cap caràcter.

lista = []
suma = 0
aprobado = float(input("¿Cual es la nota minima para aprobar?: "))
while aprobado > 10:
    aprobado = float(input("¿Cual es la nota minima para aprobar?: "))
while True:
    x = input("Dime notas aleatorias: ")
    if x.isdigit():
        if int(x) >= aprobado and int(x) <= 10:
            x = int(x)
            lista += [x]
    else:
        break
for i in lista:
    suma += i
nota = suma/len(lista)

print("La media de todos los números son ", nota)