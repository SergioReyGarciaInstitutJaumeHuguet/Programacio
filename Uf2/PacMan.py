import keyboard, time
from os import system
# Omplo la matriu
def omplirMatriu(a):
    global matrix
    matrix = [[a for i in range(17)]for i in range(12)]
    dibuixarBordejats("*")
    matrix[coco[0]][coco[1]] = "@"
# Dibuixo els bordejats
def dibuixarBordejats(a):
    global matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0 or i == 11 or j == 16:
                matrix[i][j] = a
# Mostro la matriu
def mostrarMatriu():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
# Comprobo que el joc ha terminat
def terminar(a):
    global Terminar
    time.sleep(0.1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == puntos:
                Terminar = True
                break
            else:
                Terminar = False
        if Terminar == True: break
    mostrarMatriu()
# Funció de moure amunt, avall, a l'esquerra i la dreta
def moureAmunt():
    if matrix[coco[0]-1][coco[1]] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.5)
    else:
        matrix[coco[0]][coco[1]] = " "
        coco[0]-=1
        matrix[coco[0]][coco[1]] = "@"
def moureAvall():
    if matrix[coco[0]+1][coco[1]] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.5)
    else:
        matrix[coco[0]][coco[1]] = " "
        coco[0]+=1
        matrix[coco[0]][coco[1]] = "@"
def moureEsquerra():
    if matrix[coco[0]][coco[1]-1] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.5)
    else:
        matrix[coco[0]][coco[1]] = " "
        coco[1]-=1
        matrix[coco[0]][coco[1]] = "@"
def moureDreta():
    if matrix[coco[0]][coco[1]+1] == "*":
        print("NO POTS PASSAR")
        time.sleep(0.5)
    else:
        matrix[coco[0]][coco[1]] = " "
        coco[1]+=1
        matrix[coco[0]][coco[1]] = "@"

coco = [1,1] # Es la posició on hi es el personatge principal
Terminar = True
puntos = "-" # Punts que es tenen que menjar el personatge 
omplirMatriu(puntos) # Omplo la matriu amb els punts que jo vull posar
mostrarMatriu()
while Terminar:
    if keyboard.is_pressed('w') or keyboard.is_pressed('W'):
        moureAmunt()
        system("cls") #Això es per esborrar l'anterior taula
        terminar(puntos)
    if keyboard.is_pressed('a') or keyboard.is_pressed('A'):
        moureEsquerra()
        system("cls")
        terminar(puntos)
    if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
        moureAvall()
        system("cls")
        terminar(puntos)
    if keyboard.is_pressed('d') or keyboard.is_pressed('D'):
        moureDreta()
        system("cls")
        terminar(puntos)
    if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
        Temrinar = True
print("Felicitats, has terminat el joc")