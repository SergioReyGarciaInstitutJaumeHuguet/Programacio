#Realitza un programa que demani per teclat el resultat (dada sencer) obtingut a llançar un dau de sis cares i mostri per pantalla el nombre en lletres (dada cadena) de la cara oposada a el resultat obtingut.
#Nota 1: En les cares oposades d'un dau de sis cares estan els números: 1-6, 2-5 i 3-4.
#Nota 2: Si el nombre de el dau introduït és menor que 1 o més gran que 6, es mostrarà el missatge: "ERROR: nombre incorrecte.".
#exemple:
#Introduïu nombre de el dau: 5
#A la cara oposada hi ha el "dos".

for i in range(0,6):
    y = i
    a = int(input("Número del dado: "))
    if a == 1:
        x = "seis"
    elif a == 2:
        x = "cinco"
    elif a == 3:
        x = "cuatro"
    elif a == 4:
        x = "tres"
    elif a == 5:
        x = "dos"
    elif a == 6:
        x = "uno"
    else:
        print("ERROR: nombre incorrecte.")
        i = i-1
    print(f"Su contraparte es {x}")