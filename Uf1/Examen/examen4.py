#Ejercicio 4

a = input("Dime algo: ")
count = 0
x = 0
for i in a:
    if i == "a" or i == "A" and x == 0:
        x += 1
    if i == "b" or i == "B" and x == 1:
        x += 1
    if i == "c" or i == "C" and x == 2:
        count += 1
        x = 0
    if x == 1 and a != "b" or a != "B":
        x = 0 
    if x == 2 and a != "c" or a != "C":
        x = 0
print(f'Las letras "ABC" salen {count} veces')