num1 = 0
num2 = 0
x = False
z = 0
while x == False:
    num1 = int(input("Dime un número que sumar: "))
    num2 = int(input("Dime otro número que sumar: "))
    if num1 == 0 and num2 == 0:
        x = True
        continue
    z = num1 + num2
    print(f"Tu resultado es {z}")
print("Fin del programa")
