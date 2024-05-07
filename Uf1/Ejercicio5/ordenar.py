lista = []
compr = False
seg = False
z = 0
while compr == False:
    x = input("¿Cuantos números quieres añadir? ")
    if x.isdigit():
        x = int(x)
        compr = True
    else:
        print("Solo números enteros")
for i in range(x):
    while seg == False:
        y = input("Dime números: ")
        if y.isdigit():
            y = int(y)
            lista += [y]
            z += 1
        else:
            print("Solo números enteros")
        if z == x:
            seg = True
listaaux = []
for j in range(0, len(lista)):
    for i in range(0, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
print(lista)