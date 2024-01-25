#Escriure per pantalla cada caràcter d'una cadena introduïda per teclat, 
#primer en línies diferents i després en una única línia.
a = input("Dime una frase: ")
for i in a:
    print(i)
for i in a:
    print(i, end="")