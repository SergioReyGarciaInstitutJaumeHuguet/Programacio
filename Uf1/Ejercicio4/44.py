#Suposant que hem introduït una cadena per teclat que representa una frase (paraules separades per espais), 
#realitza un programa que compti quantes paraules té.
frase = input("Dime una frase")
cont = 0
for i in frase:
    if i == ' ':
        cont+=1
print(cont)