#Escriu un programa que llegeixi un nombre i indiqui si és parell o imparell.

a = int(input("Introduce un número: "))
a %= 2
if a == 0:
    print("Es parell")
else:
    print("Es imparell")