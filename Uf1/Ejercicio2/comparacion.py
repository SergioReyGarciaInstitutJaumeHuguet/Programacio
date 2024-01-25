# Algorisme que demani dos nombres i indiqui si el primer és més gran que el segon o no.

num1 = int(input("Dame un primer número: "))
num2 = int(input("Dame un segundo número: "))
if num1 > num2:
    print("El primer número es más grande")
elif num2 > num1:
    print("El primer número no es más grande")
else:
    print("Los dos números son iguales")