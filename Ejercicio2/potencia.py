# Realitza un algoritme que calculi la potència, per això demana per teclat la base i l'exponent. Poden ocórrer tres coses:
# L'exponent sigui positiu, només has d'imprimir la potència.
# L'exponent sigui 0, el resultat es 1.
# L'exponent sigui negatiu, el resultat es 1 / potència amb l'exponent positiu.
a = int(input("Dame la base: "))
b = int(input("Dame la exponente: "))
if b>0:
    print(f"El resultat es: {pow(a,b)}")
elif b == 0:
    print("El resultado es 1")    
else:
    print(f"El resultat es: {1/(pow(a,abs(b)))}")