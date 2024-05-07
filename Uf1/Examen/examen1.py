# Ejercicio 1

x = int(input("Dime un número superior a 2: "))
a = 0
while x < 3:
    if x > 3:
       break
    elif x < 3:
       x = int(input("Dime un número superior a 2: "))
a = x/3
print(f"Hay {a} multiplos de 3 (3 * {a} = {x})")
