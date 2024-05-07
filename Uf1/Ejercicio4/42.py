#Realitzar un programa que comprova si una cadena llegida per teclat comença per una subcadena introduïda per teclat.
cadena = input("Dime una cosa: ")
subcadena = input("Mas corta: ")

igual = True
x = len(subcadena)
for i in range(len(subcadena)):
    if cadena[i] != subcadena[i]:
        igual = False
        break

if igual == True:
    print("Si")
else:
    print("No")