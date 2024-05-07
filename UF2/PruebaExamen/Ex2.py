def llenar():
    global b
    if b >= countNum:
        b = -1
    b += 1

def frase(a):
    global llistanum
    llistanum = []
    limpia = a.replace(",", "").replace(":", " ").replace("¿", "").replace("?", "").replace(".","")
    for i in limpia.split():
        if i.isdigit(): llistanum.append(int(i))
    preguntaCantidad()

def preguntaCantidad():
    global countNum
    global matrix
    while True:
        countNum = input("Cuantos números vas a meter: ")
        if countNum.isdigit(): 
            countNum = int(countNum)
            break
        else: print("Solo números")
    matrix = [[" " for i in range(2)]for i in range(countNum)]
    preguntanum()

def preguntanum():
    global matrix
    global b
    for i in range(countNum):
        while True:
            num = input(f"Dime el número {i+1}: ")
            if num.isdigit(): 
                num = int(num)
                break
            else: print("Solo números")
        matrix[b][c] = num
        llenar()
    verificar()

def verificar():
    global matrix
    for i in range(countNum):
        a = 0
        llenar()
        for j in llistanum:
            if j == matrix[b][c]:
                a += 1
        matrix[b][c+1] = a
    mostrar()

def mostrar():
    a = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a = not a
            if a:
                print(matrix[i][j], end=": ")
            else:
                print(matrix[i][j], end="")
        print()

b = 0
c = 0

frase("En el amplio cielo celeste, adornado con esponjosas nubes blancas, conté 8 nubes dispersas mientras paseaba por el parque. Allí, en el área de juegos, había 12 niños riendo y jugando: 4 columpios, 3 toboganes y 1 césped salpicado de margaritas los entretenían. Al detenerme junto a la fuente central, vi 10 patos nadando y 7 peces saltando entre las plantas acuáticas. Alrededor del parque, conté 6 bancos de madera y 4 altas farolas. Entre los árboles que bordeaban el parque, divisé un grupo de 15 pájaros revoloteando. Finalmente, al mirar el reloj de la torre en la entrada, noté que eran las 3:45 p.m., con sus agujas de bronce marcando el tiempo con precisión. Mientras deambulaba por el pintoresco sendero de un parque en una soleada tarde de primavera, me propuse hacer un recuento meticuloso de todos los números a mi alrededor. En el vasto cielo azul, adornado con caprichosas nubes blancas, conté un total de 8 nubes flotando de manera dispersa. Al llegar al área de juegos infantiles, me encontré con una animada congregación de 12 niños, cada uno sumergido en su propio juego, algunos balanceándose en los 4 columpios disponibles, otros deslizándose por los 3 toboganes coloridos y el resto correteando por el césped salpicado de margaritas. Me detuve junto a una fuente central, donde el agua fresca brotaba en una danza rítmica, y allí avisté 10 patos nadando plácidamente en su superficie, mientras que 7 peces de colores jugueteaban entre las plantas acuáticas. Alrededor del parque, conté con atención 6 bancos de madera estratégicamente ubicados, proporcionando descanso a los visitantes cansados. Además, noté la presencia de 4 farolas altas, cuyas luces comenzaban a parpadear con la llegada del atardecer. Mirando hacia arriba, entre los 6 árboles robustos que bordeaban el perímetro del parque, vi alegremente revolotear a un grupo de 15 pájaros, cada uno cantando su propia melodía. Finalmente, al consultar el reloj de la torre que se alzaba majestuosamente en la entrada principal del parque, me percaté de que marcaba las 3:45 p.m., con sus agujas de bronce avanzando con precisión hacia el siguiente minuto.")
