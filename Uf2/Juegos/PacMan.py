import keyboard, time, random, time
from os import system
# Pregunto al usuari l'altura i anchura que vol a la taula, corroborant que siguin números i no lletres
def taula():
    global altura
    global anchura
    global tauler
    num = []
    for i in range(10):
        num.append(str(i))
    while True:
        while True:
            boleano = True
            altura = input("Altura del tauler: ")
            for i in altura:
                if i not in num:
                    print("ERROR")
                    print("Has de posar números enters")
                    boleano = False
                    break
            if boleano == True:
                altura = int(altura)
                break
        while True:
            boleano = True
            anchura = input("Anchura del tauler: ")
            for i in anchura:
                if i not in num:
                    print("ERROR")
                    print("Has de posar números enters")
                    boleano = False
                    break
            if boleano == True:
                anchura = int(anchura)
                break
        tauler = (altura * anchura)
        if altura > 2 and anchura > 2:
            tauler -= 5
            break
        else:
            system("cls")
            print("ERROR")
            print("El tablero no puede tener menos de 6 cuadros vacíos")

# Omplo la matriu
def omplirMatriu(a):
    global matrix
    matrix = [[a for i in range(anchura + 2)]for i in range(altura + 2)]
    dibuixarBordejats("*")
    matrix[coco[0]][coco[1]] = "@"
# Dibuixo els bordejats
def dibuixarBordejats(a):
    global matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0 or i == altura+1 or j == anchura+1:
                matrix[i][j] = a
    premi()

# Premi
def premi():
    global matrix
    while True:
        a = 0
        num1 = []
        num2 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != 0 and j != 0 and i != altura+1 and j != anchura+1:
                    num1.append(i)
                    num2.append(j)
                    a += 1
        if a >= 5:
            break
    
    premi1 = []
    premi2 = []
    for i in range(5):
        premiNum = random.choice(num1)
        premi1.append(premiNum)
        num1.remove(premiNum)

        premiNum = random.choice(num2)
        premi2.append(premiNum)
        num2.remove(premiNum)
        matrix[premi1[i]][premi2[i]] = premiSimbol

# Mostro la matriu
def mostrarMatriu():
    global tauler
    global Punts
    print(f"Punts: {Punts}")
    print(f"Casilles: {tauler}")
    print(f"Posició: {coco}")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

# Comprobo que el joc ha terminat
def terminar(a):
    global Terminar
    global tauler
    if anterior == a:
        tauler -= 1
    if PuntsPremi == 0:
        Terminar = False
    mostrarMatriu()

# Funció de moure amunt, avall, a l'esquerra i la dreta
def moureAmunt():
    global anterior
    global PuntsPremi
    global Punts
    anterior = matrix[coco[0]-1][coco[1]]
    if matrix[coco[0]-1][coco[1]] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.3)
    else:
        if matrix[coco[0]-1][coco[1]] == premiSimbol: 
            PuntsPremi -= 1
            Punts += 1000
        matrix[coco[0]][coco[1]] = " "
        coco[0]-=1
        matrix[coco[0]][coco[1]] = "@"
def moureAvall():
    global anterior
    global PuntsPremi
    global Punts
    anterior = matrix[coco[0]+1][coco[1]]
    if matrix[coco[0]+1][coco[1]] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.3)
    else:
        if matrix[coco[0]+1][coco[1]] == premiSimbol: 
            PuntsPremi -= 1
            Punts += 1000
        matrix[coco[0]][coco[1]] = " "
        coco[0]+=1
        matrix[coco[0]][coco[1]] = "@"
def moureEsquerra():
    global anterior
    global PuntsPremi
    global Punts
    anterior = matrix[coco[0]][coco[1]-1]
    if matrix[coco[0]][coco[1]-1] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.3)
    else:
        if matrix[coco[0]][coco[1]-1] == premiSimbol: 
            PuntsPremi -= 1
            Punts += 1000
        matrix[coco[0]][coco[1]] = " "
        coco[1]-=1
        matrix[coco[0]][coco[1]] = "@"
def moureDreta():
    global anterior
    global PuntsPremi
    global Punts
    anterior = matrix[coco[0]][coco[1]+1]
    if matrix[coco[0]][coco[1]+1] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.3)
    else:
        if matrix[coco[0]][coco[1]+1] == premiSimbol: 
            PuntsPremi -= 1
            Punts += 1000
        matrix[coco[0]][coco[1]] = " "
        coco[1]+=1
        matrix[coco[0]][coco[1]] = "@"

taula()
coco = [1,1] # Es la posició on hi es el personatge principal
Terminar = True
fons = "-" # Es el fons del tauler
premiSimbol = "$"
PuntsPremi = 5
Punts = 0
tempsInici = time.time()
omplirMatriu(fons) # Omplo la matriu amb els fons que jo vull posar
mostrarMatriu()
while Terminar:
    time.sleep(0.05)
    if keyboard.is_pressed('w') or keyboard.is_pressed('W'):
        moureAmunt()
        system("cls") #Això es per esborrar l'anterior taula
        terminar(fons)
    if keyboard.is_pressed('a') or keyboard.is_pressed('A'):
        moureEsquerra()
        system("cls")
        terminar(fons)
    if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
        moureAvall()
        system("cls")
        terminar(fons)
    if keyboard.is_pressed('d') or keyboard.is_pressed('D'):
        moureDreta()
        system("cls")
        terminar(fons)
    if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
        Terminar = False
print("Felicitats, has terminat el joc")
print(f"Temps: {round(time.time() - tempsInici, 2)} segons")