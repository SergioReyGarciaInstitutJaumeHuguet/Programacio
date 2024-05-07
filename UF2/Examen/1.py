import random

def database(): #Creo una función que llene automáticamente la matriz con nombres
    global matrix
    name = ["juan", "jose", "sergio", "miquel", "cervantes", "pol", "aiinhoa", "alex", "axel", "leo"]
    for i in range(10): #Escojo el nombre de forma random y lo añado a la matriz
        randomName = random.choice(name)
        for j in range(len(name)): #No me acuerdo del nombre de la función que eliminaba el nombre de la lista, así que lo elimino de esta forma
            if randomName == name[j-1]: name.pop(j-1)
        matrix[i][0] = randomName
        matrix[i][1] = "1234" #Le pongo la misma contraseña a todos

def login(): #Pregunto el usuario y la contraseña y verifico si son correctos
    a = 0 #Para saber si ha entrado dentro del primer if
    user = input("Nom d'usuari: ")
    password = input("Contrasenya: ")
    for i in range(len(matrix)):
        if user == matrix[i][0]:
            a += 1
            if password == matrix[i][1]: return 1
            else: return 0
    if a > 1: return 0

matrix = [[" " for i in range(2)]for i in range(10)]
error = 0

database()
while True:
    if login() == 1: 
        print("Bienvenido")
        break
    else: 
        error += 1
        print("Usuari o contrasenya incorrecta")
    if error >= 3:
        print("Intents terminats")
        break