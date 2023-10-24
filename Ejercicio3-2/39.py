#Algorisme que llegeixi nombres enters fins trobar 0, i ens mostri el màxim, el mínim i la mitjana de tots ells. 
#Pensa com haurem d'inicialitzar les variables.
a = 1
b = 0
p = 0
suma = 0
mediana = 0
max = 0
min = 0
while a != 0:
    a = int(input("Dime un número entero hasta llegar a 0: "))
    if p == 1 and a != 0:
        min = max
    if a == 0:
        if p == 0:
            p+=1
        mediana = suma / p
        continue
    elif min > a:
        min = a
    elif a > max:
        max = a
    suma += a
    p+=1
print(f"La mediana es {mediana}")
print(f"El máximo es {max}")
print(f"El mínimo es {min}")