def quicksort(arr, dato):
    if len(arr) <= 1:
        return arr
    else:
        # S'escull el primer element com a pivot
        pivot = arr[0]

        # Es creen dues llistes, una pels elements menors o iguals al pivot i una altra pels majors
        lesser = []
        greater = []

        for i in range(1, len(arr)):
            if arr[i][dato] <= pivot[dato]:
                lesser.append(arr[i])
            else:
                greater.append(arr[i])

        # S'aplica recursivament Quicksort a les subllistes menor i major
        return quicksort(lesser, dato) + [pivot] + quicksort(greater, dato)

def introduir():
    empleado = {}
    lista = quicksort(bombers, "id")
    id = lista[-1]["id"]+1
    empleado["id"] = id
    nombre = input("Nombre: ")
    empleado["nombre"] = nombre
    apellido = input("Apellido: ")
    empleado["apellido"] = apellido
    horas = int(input("Horas: "))
    empleado["horas"] = horas
    bombers.append(empleado)

def modificar():
    global bombers
    encontrar = False
    valor = 0
    id_modificar = int(input("Dime el id de la persona que quieres modificar\n"))
    for i in bombers:
        if id_modificar == i['id']:
            encontrar = True
            valor = bombers.index(i)
    if encontrar == True:
        print(f"Que horas le quieres asignar al usuario {bombers[valor]['nombre']}")
        horas = int(input())
        bombers[valor]['horas'] = horas
    else:
        print("ERROR - ID no trobat")

def mostrar():
    global bombers
    orden = quicksort(bombers, "horas")
    for bomber in orden:
        for clau, valor in bomber.items():
            print(clau + ":", valor)
        print()
bombers = [
    {
        "id": 1,
        "nombre": "Paco",
        "apellido": "Mangueras",
        "horas": 6
    },
    {
        "id": 2,
        "nombre": "Alex",
        "apellido": "Tintor",
        "horas": 3
    },
    {
        "id": 3,
        "nombre": "Elsa",
        "apellido": "Patilla",
        "horas": 15
    },
    {
        "id": 4,
        "nombre": "Jordi",
        "apellido": "Bord",
        "horas": 2
    }
]


while True:
    opcion = input("1. Introduir nou bomber amb hores\n" \
        "2. Modificar hores del bomber donada la id\n" \
        "3. Llistar bombers (ordenats amb el mètode quicksort que se us proporciona)\n" \
        "4. Sortir\n")

    if opcion == "1":
        introduir()
    elif opcion == "2":
        modificar()
    elif opcion == "3":
        mostrar()
    elif opcion == "4":
        break
    else:
        print("ERROR - Opción no válida")