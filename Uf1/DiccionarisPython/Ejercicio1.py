dicc = {}
x = int(input("Dime la cantidad de números que quieres añadir: "))
x += 1
for i in range(x):
    if i == 0:
        continue
    y = pow(i,2)
    dicc[i] = y
    print(dicc[i])