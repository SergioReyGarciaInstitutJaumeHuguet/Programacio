import random
lista = []
max = 1000
min = 1
for i in range(max):
    lista.append(i+1)
numAleatori = random.choice(lista)
intentos = 10
ganar = False
perder = False
a = 0
def juego():
    global a
    global respuesta
    print(f"Número de intentos: {intentos}")
    respuesta = input(f"Dime un número entre {min} y {max}\n")
    if respuesta.isdigit() == False:
        print(f"Solo se permiten números del {min} al {max}")
        juego()
    respuesta = int(respuesta)
    if respuesta >= {min} and respuesta <= {max}:
        comprobar()
        if ganar == True:
            if a == 0:
                print(f"Has acertado con {10-intentos} intentos")
                a += 1
        elif perder == True:
            print("Has perdido")
        else:
            juego()

def comprobar():
    global intentos
    global ganar
    global perder
    if intentos == 0:
        perder = True
    elif respuesta == numAleatori:
        ganar = True
    elif respuesta < numAleatori:
        print("Es un número más grande")
        intentos -= 1
    else:
        print("Es un número más pequeño")
        intentos -= 1

juego()