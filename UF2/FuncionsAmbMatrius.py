matrix = [["-" for i in range(2)]for i in range(4)]
fila = 0
columna = 0
a = True
def imprimirTaula():
    global a
    if a:
        for i in range(4):
            for j in range(2):
                print(matrix[i][j], end=" ")
            print()
        a = False
    else:
        for j in range(2):
            for i in range(4):
                print(matrix[i][j], end=" ")
            print()
        a = True

def verificar(filaNum = [], columnaNum = []):
    for i in range(5):
        if i == 0:
            continue
        filaNum.append(str(i))
    for i in range(3):
        if i == 0:
            continue
        columnaNum.append(str(i))
    global fila
    global columna
    while True:
        fila = input("¿Que fila quieres modificar?\n")
        if fila in filaNum:
            fila = int(fila) - 1
            columna = input("¿Que columna quieres modificar?\n")
            if columna not in columnaNum:
                print("ERROR")
                print("La columna solo puede ser 1 o 2")
            else:
                columna = int(columna) - 1
                break
        else:
            print("ERROR")
            print("La fila solo puede ser 1, 2, 3 o 4")

def afegirFicha():
    salir = False
    numeros = []
    for i in range (10):
        numeros.append(str(i))
    while True:
        ficha = input("¿Que número quieres añadir?\n")
        for i in ficha:
            if i not in numeros:
                print("Solo se aceptan números")
                salir = True
                break
        if salir == False:
            ficha = int(ficha)
            matrix[fila][columna] = ficha
            break

def afegirElement():
    verificar()
    if matrix[fila][columna] != "-":
        print("ERROR")
        print("ESPACIO OCUPADO")
    else:
        afegirFicha()

def modificarElement():
    verificar()
    if matrix[fila][columna] == "-":
        print("ERROR")
        print("ESPACIO SIN OCUPAR")
    else:
        afegirFicha()

def eliminarElement():
    verificar()
    matrix[fila][columna] == "-"

def imprimirStats():
    max = matrix[0][0]
    min = matrix[0][0]
    suma = 0
    roto = False
    for i in range(4):
        for j in range(2):
            if matrix[i][j] == "-":
                roto = True
                break
            if matrix[i][j] > max:
                max = int(matrix[i][j])
            if matrix[i][j] < min:
                min = int(matrix[i][j])
            suma += int(matrix[i][j])
    mediana = suma / 8
    if roto == False:
        print(f"Max: {max}")
        print(f"Min: {min}")
        print(f"Suma: {suma}")
        print(f"Mediana: {mediana}")

while True:
    print("Que opción quieres:")
    print("1: Añadir elemento")
    print("2: Modificar elemento")
    print("3: Eliminar elemento")
    print("4: Mostrar tabla")
    print("5: Imprimir estadisticas")
    print("6: Salir")
    opcion = input()

    if opcion == "1":
        afegirElement()
    elif opcion == "2":
        modificarElement()
    elif opcion == "3":
        eliminarElement()
    elif opcion == "4":
        imprimirTaula()
    elif opcion == "5":
        imprimirStats()
    elif opcion == "6":
        break
