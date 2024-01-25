#Realitzar un programa que donada una cadena de caràcters per caràcters, 
#generi una altra cadena resultat d'invertir la primera. S'ha de fer sense Slice ([::-1])
frase = input("Dime una frase: ")
reves = ""
for i in range(len(frase)-1, -1, -1):
    reves += frase[i]
print(reves)