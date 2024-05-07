import random
bucle = True
print("BINGO")
print("Escoje números entre el 1 y el 9 sin repetir ningúno")
# Pido los números y compruebo que estén en el rango. Lo compruebo con string porque con un int se puede petar el programa
while bucle:
    num1 = input("Dime el número 1\n")
    
    if num1 != "1" and num1 != "2" and num1 != "3" and num1 != "4" and num1 != "5" and num1 != "6" and num1 != "7" and num1 != "8" and num1 != "9":
        continue
    num2 = input("Dime el número 2\n")
    if num2 != "1" and num2 != "2" and num2 != "3" and num2 != "4" and num2 != "5" and num2 != "6" and num2 != "7" and num2 != "8" and num2 != "9":
        continue
    num3 = input("Dime el número 3\n")
    if num3 != "1" and num3 != "2" and num3 != "3" and num3 != "4" and num3 != "5" and num3 != "6" and num3 != "7" and num3 != "8" and num3 != "9":
        continue
    num4 = input("Dime el número 4\n")
    if num4 != "1" and num4 != "2" and num4 != "3" and num4 != "4" and num4 != "5" and num4 != "6" and num4 != "7" and num4 != "8" and num4 != "9":
        continue
    if num1 == num2 or num2 == num3 or num3 == num4 or num4 == num1 or num4 == num2:
        continue
    bucle = False
# Estos son los números que el usuario verá
verNum1 = num1
verNum2 = num2
verNum3 = num3
verNum4 = num4
# Hago la lista de números con la ley del vago
numeros = []
for i in range(9):
    numeros.append(i+1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
Terminar = False
while Terminar == False:
    numeroPremiado = random.choice(numeros)
    print(f"Número aleatorio: {numeroPremiado}")
    # Los números acertados los cambio a 0 para que no pete el programa
    if numeroPremiado == int(num1):
        num1 = 0
        verNum1 = "X"
    elif numeroPremiado == int(num2):
        num2 = 0
        verNum2 = "X"
    elif numeroPremiado == int(num3):
        num3 = 0
        verNum3 = "X"
    elif numeroPremiado == int(num4):
        num4 = 0
        verNum4 = "X"
    print(verNum1, verNum2, verNum3, verNum4)
    if num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0:
        print("BINGO")
        print("Has ganado")
        Terminar = True