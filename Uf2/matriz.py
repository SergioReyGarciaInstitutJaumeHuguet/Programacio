import random;
juego = True
print("TRES EN RAYA")
while juego:
    matrix = [["-" for i in range(3)]for i in range(3)] #Cada vez que entre al menú para cambiar el juego, se creará una matriz de 3X3
    print("¡Hola jugador!\nEscoje una de estas opciónes")
    print("1 - Modo Express")
    print("2 - Modo Classic")
    print("3 - Modo Forever Alone")
    print("4 - Información")
    print("5 - Salir")
    opcion = input() #Esta variable la usaré siempre que deba guardar alguna información momentanea
    if opcion == "1":
        J1 = input("¿Cual es tu nombre Jugador 1?\n")
        J2 = input("¿Cual es tu nombre Jugador 2?\n")
        opcion = random.choice([J1,J2])
        print(f"Empieza {opcion}")
        if opcion == J1:
            opcion2 = J2 #Esta opción la usaremos para almacenar el nombre del segundo jugador
        else:
            opcion2 = J1
        juegoOpcion1 = True
        while juegoOpcion1:
            for linea in matrix:
                for columna in linea:
                    print(columna, end=" ")
                print()
            print()
        #Le pregunto al jugador 1 que fila y columna quiere cambiar, comprobando que son los números 1, 2 o 3 y verificando que la posición no esté usada
            seleccionFila = input(f"Dime la fila a la que quieres añadir la ficha {opcion} con la ficha X\n")
            if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                seleccionFila = int(seleccionFila)-1
            else:
                continue
            seleccionColumna = input(f"Dime la columna a la que quieres añadir la ficha {opcion} con la ficha X\n")
            if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                seleccionColumna = int(seleccionColumna)-1
            else:
                continue
            if matrix[seleccionFila][seleccionColumna] == "X" or matrix[seleccionFila][seleccionColumna] == "O":
                continue
            else:
                matrix[seleccionFila][seleccionColumna] = "X"
            print(f"\n{opcion}:")
            print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
            for linea in matrix:
                for columna in linea:
                    print(columna, end=" ")
                print()
        #Compruebo si ha ganado el jugador 1
            if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
                print(f"\nHa ganado {opcion}")
                juegoOpcion1 = False
                continue
        #Compruebo si hay empate
            opcion3 = False #Este lo usaremos para darle un break
            for linea in matrix:
                if opcion3 == True:
                    break
                for columna in linea:
                    if columna == "-":
                        juegoOpcion1 = True
                        opcion3 = True
                        break
                    else:
                        juegoOpcion1 = False
            if juegoOpcion1 == False:
                print("EMPATE")
                print()
                break
        #Le pregunto al jugador 2 que fila y columna quiere cambiar, comprobando que son los números 1, 2 o 3 y verificando que la posición no esté usada
            seleccionJ2 = True
            while seleccionJ2:
                seleccionFila = input(f"Dime la fila a la que quieres añadir la ficha {opcion2} con la ficha O\n")
                if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                    seleccionFila = int(seleccionFila)-1
                else:
                    continue
                seleccionColumna = input(f"Dime la columna a la que quieres añadir la ficha {opcion2} con la ficha O\n")
                if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                    seleccionColumna = int(seleccionColumna)-1
                else:
                    continue
                if matrix[seleccionFila][seleccionColumna] == "X" or matrix[seleccionFila][seleccionColumna] == "O":
                    continue
                else:
                    seleccionJ2 = False
                    matrix[seleccionFila][seleccionColumna] = "O"
            print(f"\n{opcion2}:")
            print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
        #Compruebo si ha ganado el jugador 2
            if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
                print(f"\nHa ganado {opcion2}")
                juegoOpcion1 = False
                continue
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    elif opcion == "2":
        vueltaJ1 = 0 #Creo una variable para contar las vueltas de cada jugador
        vueltaJ2 = 0
        vuelta = True
        J1 = input("¿Cual es tu nombre Jugador 1?\n")
        J2 = input("¿Cual es tu nombre Jugador 2?\n")
        opcion = random.choice([J1,J2])
        print(f"Empieza {opcion}")
        if opcion == J1:
            opcion2 = J2 #Esta opción la usaremos para almacenar el nombre del segundo jugador
        else:
            opcion2 = J1
        juegoOpcion1 = True
        while juegoOpcion1:
            for linea in matrix:
                for columna in linea:
                    print(columna, end=" ")
                print()
            print()
            while vuelta:
                if vueltaJ1 == 3 and vueltaJ2 == 3:
                    vuelta = False
                    continue
            #Le pregunto al jugador 1 que fila y columna quiere cambiar, comprobando que son los números 1, 2 o 3 y verificando que la posición no esté usada
                seleccionFila = input(f"Dime la fila a la que quieres añadir la ficha {opcion} con la ficha X\n")
                if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                    seleccionFila = int(seleccionFila)-1
                else:
                    continue
                seleccionColumna = input(f"Dime la columna a la que quieres añadir la ficha {opcion} con la ficha X\n")
                if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                    seleccionColumna = int(seleccionColumna)-1
                else:
                    continue
                if matrix[seleccionFila][seleccionColumna] == "X" or matrix[seleccionFila][seleccionColumna] == "O":
                    continue
                else:
                    vueltaJ1+=1
                    matrix[seleccionFila][seleccionColumna] = "X"
                print(f"\n{opcion}:")
                print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
                for linea in matrix:
                    for columna in linea:
                        print(columna, end=" ")
                    print()
            #Le pregunto al jugador 2 que fila y columna quiere cambiar, comprobando que son los números 1, 2 o 3 y verificando que la posición no esté usada
                seleccionJ2 = True
                while seleccionJ2:
                    seleccionFila = input(f"Dime la fila a la que quieres añadir la ficha {opcion2} con la ficha O\n")
                    if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                        seleccionFila = int(seleccionFila)-1
                    else:
                        continue
                    seleccionColumna = input(f"Dime la columna a la que quieres añadir la ficha {opcion2} con la ficha O\n")
                    if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                        seleccionColumna = int(seleccionColumna)-1
                    else:
                        continue
                    if matrix[seleccionFila][seleccionColumna] == "X" or matrix[seleccionFila][seleccionColumna] == "O":
                        continue
                    else:
                        vueltaJ2+=1
                        seleccionJ2 = False
                        matrix[seleccionFila][seleccionColumna] = "O"
                print(f"\n{opcion2}:")
                print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
                for linea in matrix:
                    for columna in linea:
                        print(columna, end=" ")
                    print()
            cambio = True #Creo esta variable para tener el bucle de cambiar la ficha
            filaCambiar = 0 #Creo esta variable para cambiar el valor de la fila por un "-"
            columnaCambiar = 0 #Creo esta variable para cambiar el valor de la columna por un "-"
            while cambio:
                #Compruebo si ha ganado el jugador 1
                if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
                    print(f"\nHa ganado {opcion}")
                    cambio = False
                    juegoOpcion1 = False
                    continue
                #Compruebo si ha ganado el jugador 2
                if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
                    print(f"\nHa ganado {opcion2}")
                    cambio = False
                    juegoOpcion1 = False
                    continue
                seleccionFila = input(f"Dime la fila en donde está la ficha que quieres cambiar {opcion} con la ficha X\n")
                if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                    seleccionFila = int(seleccionFila)-1
                    filaCambiar = seleccionFila
                else:
                    continue
                seleccionColumna = input(f"Dime la columna en donde está la ficha que quieres cambiar {opcion} con la ficha X\n")
                if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                    seleccionColumna = int(seleccionColumna)-1
                    columnaCambiar = seleccionColumna
                else:
                    continue
                if matrix[seleccionFila][seleccionColumna] == "X":
                    seleccionFila = input(f"Dime la fila a la que quieres mover la ficha {opcion} con la ficha X\n")
                    if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                        seleccionFila = int(seleccionFila)-1
                    else:
                        continue
                    seleccionColumna = input(f"Dime la columna a la que quieres mover la ficha {opcion} con la ficha X\n")
                    if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                        seleccionColumna = int(seleccionColumna)-1
                    if matrix[seleccionFila][seleccionColumna] == "-":
                        matrix[seleccionFila][seleccionColumna] = "X"
                        matrix[filaCambiar][columnaCambiar] = "-"
                    else:
                        print("Has seleccionado una casilla que no estaba vacía")
                        continue
                print(f"\n{opcion}:")
                print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
                for linea in matrix:
                    for columna in linea:
                        print(columna, end=" ")
                    print()
                #Compruebo si ha ganado el jugador 1
                if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
                    print(f"\nHa ganado {opcion}")
                    cambio = False
                    juegoOpcion1 = False
                    continue
                #Compruebo si ha ganado el jugador 2
                if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
                    print(f"\nHa ganado {opcion2}")
                    cambio = False
                    juegoOpcion1 = False
                    continue
                seleccionFila = input(f"Dime la fila en donde está la ficha que quieres cambiar {opcion2} con la ficha O\n")
                if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                    seleccionFila = int(seleccionFila)-1
                    filaCambiar = seleccionFila
                else:
                    continue
                seleccionColumna = input(f"Dime la columna en donde está la ficha que quieres cambiar {opcion2} con la ficha O\n")
                if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                    seleccionColumna = int(seleccionColumna)-1
                    columnaCambiar = seleccionColumna
                else:
                    continue
                if matrix[seleccionFila][seleccionColumna] == "O":
                    seleccionFila = input(f"Dime la fila a la que quieres mover la ficha {opcion2} con la ficha O\n")
                    if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
                        seleccionFila = int(seleccionFila)-1
                    else:
                        continue
                    seleccionColumna = input(f"Dime la columna a la que quieres mover la ficha {opcion2} con la ficha O\n")
                    if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
                        seleccionColumna = int(seleccionColumna)-1
                    if matrix[seleccionFila][seleccionColumna] == "-":
                        matrix[seleccionFila][seleccionColumna] = "O"
                        matrix[filaCambiar][columnaCambiar] = "-"
                    else:
                        print("Has seleccionado una casilla que no estaba vacía")
                        continue
                print(f"\n{opcion2}:")
                print(f"Fila: {seleccionFila}\nColumna: {seleccionColumna}")
                for linea in matrix:
                    for columna in linea:
                        print(columna, end=" ")
                    print()
                #Compruebo si ha ganado el jugador 2
                if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
                    print(f"\nHa ganado {opcion2}")
                    cambio = False
                    juegoOpcion1 = False
                    continue
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    elif opcion == "3":
        for linea in matrix:
            for columna in linea:
                print(columna, end=" ")
            print()
        print()
    #Le pregunto al jugador que fila y columna quiere cambiar, comprobando que son los números 1, 2 o 3 y verificando que la posición no esté usada
        seleccionFila = input("Dime la fila a la que quieres añadir la ficha\n")
        if seleccionFila == "1" or seleccionFila == "2" or seleccionFila == "3":
            seleccionFila = int(seleccionFila)-1
        else:
            continue
        seleccionColumna = input("Dime la columna a la que quieres añadir la ficha\n")
        if seleccionColumna == "1" or seleccionColumna == "2" or seleccionColumna == "3":
            seleccionColumna = int(seleccionColumna)-1
        else:
            continue
        if matrix[seleccionFila][seleccionColumna] == "X" or matrix[seleccionFila][seleccionColumna] == "O":
            continue
        else:
            matrix[seleccionFila][seleccionColumna] = "X"
        print("Jugador:")
        print(f"Fila: {seleccionFila}\n Columna: {seleccionColumna}")
    #Compruebo si ha ganado el jugador
        if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
            for linea in matrix:
                for columna in linea:
                    print(columna, end=" ")
                print()
            print("\nHa ganado el jugador")
            juego = False
            continue
    #Compruebo si hay empate
        opcion3 = False #Este lo usaremos para darle un break
        for linea in matrix:
            if opcion3 == True:
                break
            for columna in linea:
                if columna == "-":
                    juegoOpcion1 = True
                    opcion3 = True
                    break
                else:
                    juegoOpcion1 = False
        if juegoOpcion1 == False:
            print("EMPATE")
            print()
            break
    #Genero la respuesta del bot
        positionR = True
        while positionR == True:
            filaRandom = random.choice([0,1,2])
            columnaRandom = random.choice([0,1,2])
    #Compruebo si la posición escogida está siendo usada
            if matrix[filaRandom][columnaRandom] == "X" or matrix[filaRandom][columnaRandom] == "O":
                continue
            else:
                matrix[filaRandom][columnaRandom] = "O"
                positionR = False
        print("Bot:")
        print(f"Fila: {filaRandom}\n Columna: {columnaRandom}")
    #Compruebo si ha ganado el bot
        if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
            for linea in matrix:
                for columna in linea:
                    print(columna, end=" ")
                print()
            print("\nHa ganado el bot")
            juego = False
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    elif opcion == "4":
        print("\nINFORMACIÓN:")
        print("1 - Es un modo PvP (Player vs Player) donde se juega al tres en raya actual, es decir, poneis fichas hasta acabar en empate")
        print("2 - Es un modo de juego PvP (Player vs Player), donde se juega al tres en raya de la forma clásica, es decir, poniendo solo 3 fichas y moviendolas por los espacios libres del tablero")
        print("3 - Es un modo PvB (Player vs Bot) donde se juega al tres en raya actual, es decir, poneis fichas hasta acabar en empate")
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    elif opcion == "5":
        juego = False
    else:
        print("\nSolo números del 1 al 5\n")