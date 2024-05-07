from os import system
terminar = True
while terminar:
    agua = { 
        "vida": 10,
        "fuerza": 6,
        "resistencia": 10,
        "resVitalitat": 2,
        "resResistencia": 3,
        "resFuerza": 0
    }
    fuego = {
        "vida": 10,
        "fuerza": 10,
        "resistencia": 6,
        "resVitalitat": 3,
        "resResistencia": 2,
        "resFuerza": 0
    }
    tierra = {
        "vida": 10,
        "fuerza": 8,
        "resistencia": 8,
        "resVitalitat":2,
        "resResistencia": 2,
        "resFuerza": 1
    }
    monstrugo = {
        "pyrofire": fuego,
        "flame": fuego,
        "hydroia": agua,
        "swimmer": agua,
        "beast": tierra
    }
    pokemonLoop = True
    while pokemonLoop:
        a = 0
        for i in monstrugo.keys():
            a += 1
            print(f"{i} ({a})")

        pokeJ1 = input(f"¿Que pokemon eliges Jugador 1?\n")
        if pokeJ1 == "1":
            pokeJ1 = "pyrofire"
        elif pokeJ1 == "2":
            pokeJ1 = "flame"
        elif pokeJ1 == "3":
            pokeJ1 = "hydroia"
        elif pokeJ1 == "4":
            pokeJ1 = "swimmer"
        elif pokeJ1 == "5":
            pokeJ1 = "beast"
        else:
            print("Pokemon indefinido, vuelve a escojer pokemon")
            system("cls")
            continue

        pokeJ2 = input(f"¿Que pokemon eliges Jugador 2?\n")
        if pokeJ2 == "1":
            pokeJ2 = "pyrofire"
        elif pokeJ2 == "2":
            pokeJ2 = "flame"
        elif pokeJ2 == "3":
            pokeJ2 = "hydroia"
        elif pokeJ2 == "4":
            pokeJ2 = "swimmer"
        elif pokeJ2 == "5":
            pokeJ2 = "beast"
        else:
            print("Pokemon indefinido, volved a escojer pokemon los dos")
            system("cls")
            continue
        
        pokemonLoop = False

    peleaLoop = True
    a = 0

    print(f"{pokeJ1} comienza con {monstrugo[pokeJ1]['vida']} puntos de vida, {monstrugo[pokeJ1]['fuerza']} puntos de fuerza y {monstrugo[pokeJ1]['resistencia']} puntos de resistencia\n")
    print(f"{pokeJ2} comienza con {monstrugo[pokeJ2]['vida']} puntos de vida, {monstrugo[pokeJ2]['fuerza']} puntos de fuerza y {monstrugo[pokeJ2]['resistencia']} puntos de resistencia\n")

    while peleaLoop:
        a += 1
        monstrugo[pokeJ1]["resistencia"] = monstrugo[pokeJ1]["resistencia"] - monstrugo[pokeJ2]["resResistencia"]
        monstrugo[pokeJ2]["resistencia"] = monstrugo[pokeJ2]["resistencia"] - monstrugo[pokeJ1]["resResistencia"]
        monstrugo[pokeJ1]["vida"] = monstrugo[pokeJ1]["vida"] - monstrugo[pokeJ2]["resVitalitat"]
        monstrugo[pokeJ2]["vida"] = monstrugo[pokeJ2]["vida"] - monstrugo[pokeJ1]["resVitalitat"]
        monstrugo[pokeJ1]["fuerza"] = monstrugo[pokeJ1]["fuerza"] - monstrugo[pokeJ2]["resFuerza"]
        monstrugo[pokeJ2]["fuerza"] = monstrugo[pokeJ2]["fuerza"] - monstrugo[pokeJ1]["resFuerza"]
        system("cls")
        print(f"Ronda {a}")
        print(f'{pokeJ1} - Resistencia: {monstrugo[pokeJ1]["resistencia"]} Vida: {monstrugo[pokeJ1]["vida"]} Fuerza: {monstrugo[pokeJ1]["fuerza"]}')
        print(f'{pokeJ2} - Resistencia: {monstrugo[pokeJ2]["resistencia"]} Vida: {monstrugo[pokeJ2]["vida"]} Fuerza: {monstrugo[pokeJ2]["fuerza"]}')
        input('\nPress any key to continue\n')
        if monstrugo[pokeJ1]["resistencia"] <= 0:
            print(f"El jugador 1 con {pokeJ1} ha perdido con 0 puntos de resistencia")
            peleaLoop = False
        elif monstrugo[pokeJ2]["resistencia"] <= 0:
            print(f"El jugador 2 con {pokeJ2} ha perdido con 0 puntos de resistencia")
            peleaLoop = False
        elif monstrugo[pokeJ1]["vida"] <= 0:
            print(f"El jugador 1 con {pokeJ1} ha perdido con 0 puntos de vida")
            peleaLoop = False
        elif monstrugo[pokeJ2]["vida"] <= 0:
            print(f"El jugador 2 con {pokeJ2} ha perdido con 0 puntos de vida")
            peleaLoop = False
        elif monstrugo[pokeJ1]["fuerza"] <= 0:
            print(f"El jugador 1 con {pokeJ1} ha perdido con 0 puntos de fuerza")
            peleaLoop = False
        elif monstrugo[pokeJ2]["fuerza"] <= 0:
            print(f"El jugador 2 con {pokeJ2} ha perdido con 0 puntos de fuerza")
            peleaLoop = False
    bucleMenu = True
    while bucleMenu:
        print("1 - Repetir juego")
        print("2 - Salir")
        opcionMenu = input("¿Que quieres hacer?\n")
        if opcionMenu == "1":
            peleaLoop = True
            bucleMenu = False
        elif opcionMenu == "2":
            terminar = False
            bucleMenu = False
        else:
            print("Opción equivocada")