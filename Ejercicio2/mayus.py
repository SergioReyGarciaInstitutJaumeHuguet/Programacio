# Programa que llegeixi una lletra per teclat i comprovi si és una lletra majúscula.

a = int(ord(input("Dame una letra: ")))
if a >= 97 and a <= 122:
    print("No es mayuscula")
elif a >= 65 and a <= 90:
    print("Es mayuscula")
else:
    print("No me has hecho caso")