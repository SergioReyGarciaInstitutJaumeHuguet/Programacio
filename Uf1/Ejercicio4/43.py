#Demana una cadena i un caràcter per teclat (valida que sigui un caràcter) 
#i mostra totes les vegades que apareix el caràcter en la cadena.
frase = input("Dime una frase: ")
letra = input("Dime un caracter: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(contador)
