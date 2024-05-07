# TENGO ALGUNOS ERRORES EN EL CÓDIGO Y ME FALTA COMENTARLO, PERO NO ME HA DADO TIEMPO A TERMINARLO
import random
def crearMatriu(a,b):
    global matrix
    matrix = [["-" for i in range(a)]for i in range(b)]
    return matrix

def omplirMatriu(matrix):
    global guardarAltura
    global guardarAnchura
    guardarAltura = []
    guardarAnchura = []
    numsAltura = []
    numsAnchura = []

    for i in range(len(matrix)):
        numsAltura.append(i)

    for i in range(len(matrix[0])):
        numsAnchura.append(i)

    a = 0

    while a < 3:
        altura = random.choice(numsAltura)
        anchura = random.choice(numsAnchura)
        if matrix[altura][anchura] == "@": continue
        else: 
            matrix[altura][anchura] = "@"
            a += 1
            guardarAltura.append(altura)
            guardarAnchura.append(anchura)

    return matrix

def incrementar():
    mostrarMatriu()
    arrayPantalla = []
    arrayPantallaDespues = []
    for i in range(3):
        matrix[guardarAltura[i]][guardarAnchura[i]] = "-"
        arrayPantalla.append(guardarAltura)
        arrayPantalla.append(guardarAnchura)
        guardarAltura[i] += 1
        guardarAnchura[i] += 1
        arrayPantallaDespues.append(guardarAltura)
        arrayPantallaDespues.append(guardarAnchura)
        if guardarAltura[i] > len(matrix)-1 or guardarAnchura[i] > len(matrix[0])-1: 
            guardarAltura.pop(i)
            guardarAltura.pop(i)
    
    print(arrayPantalla)
    print(arrayPantallaDespues)

    for i in range(len(guardarAltura)):
        matrix[guardarAltura[i]][guardarAnchura[i]] = "@"

    mostrarMatriu()

def mostrarMatriu():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

def menu():
    while True:
        opcio = input("Que vols fer?\n0 - sortir\n1 - Incrementar la posició dels @\n2 - mostrar la matriu actual\n")
        if opcio == "0": break
        elif opcio == "1": incrementar()
        elif opcio == "2": mostrarMatriu()
        else: 
            print("Debes escojer una opción\n")


omplirMatriu(crearMatriu(5,5))
menu()