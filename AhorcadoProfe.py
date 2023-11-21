import random # Importo la librería Random para escoger una palabra aleatoria
dificultad = 1 #Nivel de dificultad
#Creo la lista de palabras (ChatGPT y palabras mías)
listaPalabras = ["CIELO", "ENSALADA", "SUEÑO", "LIBRO", "MUSICA", "VIDA", "MUERTE", "LUZ", "OSCURIDAD", "ESPERANZA", "DESESPERACION", "CALOR", "FRIO", "SABOR", "OLOR", "SILENCIO", "RUIDO", "PENSAMIENTO", "ACCION", "PALABRA", "IMAGINACION", "FANTASIA", "REALIDAD", "CREACION", "DESTRUCCION", "PASADO", "FUTURO", "AHORA", "SIEMPRE", "NUNCA", "CORAZON", "MENTE", "ALMA", "CUERPO", "FAMILIA", "AMISTAD", "AMBIENTE", "CIRCUNSTANCIA", "PROBLEMA", "SOLUCION", "DESTINO", "CAMINO", "SECRETO", "AVENTURA", "DESCUBRIMIENTO", "CONOCIMIENTO", "IGNORANCIA", "BONDAD", "MALDAD", "PAZ", "GUERRA", "ARTE", "CIENCIA", "TECNOLOGIA", "NATURALEZA", "CIUDAD", "CAMPO", "OCEANO", "MONTAÑA", "DESERTO", "BOSQUE", "ANIMAL", "PLANTA", "HOMBRE", "MUJER", "NIÑO", "ADULTO", "JOVEN", "VIEJO", "RICO", "POBRE", "GRANDE", "PEQUENO", "LARGO", "CORTO", "RAPIDO", "LENTAMENTE", "ALTO", "BAJO", "ROTO", "ENTERO", "DIFICIL", "FACIL", "FELICIDAD", "TRISTEZA", "ENFADO", "AMOR", "ODIO", "MIEDO", "VALOR", "DUDA", "CONFIANZA", "SORPRESA", "ABURRIMIENTO", "ENCEFALOGRAMA", "CABEZA", "JAUME", "MARIA", "IZAN", "ESPAÑA", "ARBOL", "MARIPOSA", "COMPUTADORA", "CATEDRAL", "ELEFANTE", "PIJAMA", "KIWI", "PELOTA", "HEROE", "BARCO", "TREN", "OSO", "MANZANA", "GORILA", "CEBRA", "LORO", "LEON", "TIGRE", "JAGUAR", "COCODRILO", "ELECCION", "HORMIGA", "AGUILA", "HALCON", "CALABAZA", "CEBOLLA", "CANGREJO", "CABALLO", "FRESA", "GATO", "PERRO", "CUCHILLO", "MAR", "RANA", "NUBE", "BICICLETA", "LAPIZ", "HORMIGON", "RATON", "LLAVE", "CAMARA", "GUITARRA", "PAJARO", "LINTERNA", "SILLA", "RELOJ", "AGUACATE", "ESMERALDA", "TELESCOPIO", "ESCORPION", "JARDINERO", "PLATILLO", "CIRCUNFERENCIA", "RINOCERONTE", "ELECTRICIDAD", "ENIGMA", "CAPUCHINO", "ALAZAN", "JABALI", "NARCISO", "GALEON", "RUBI", "OXIGENO", "SINFONIA", "CEFALOPODO", "TOBOGAN", "GUSANO", "QUIMERA", "AZULEJO", "MAJESTUOSO", "CAMELLO", "DOMINO", "SALMONELLA", "TENEBROSO", "CAMALEON", "RELOJERIA", "ALEBRIJE", "VINAGRE", "RAPSODIA", "YOGUR", "IMPERMEABLE", "AEROBICO", "TORNADO", "QUINIELA", "AMBIGUO", "PAISAJE", "TIBURON", "PENDULO", "JUBILACION", "CACAHUETE", "MISTERIO", "CARBON", "CUARTEL", "AMAPOLA", "NAVEGAR", "ACROBATA", "CACTUS", "XILOFONO", "EUCALIPTO", "OQUEDAD", "PERSIANA", "EXOTICO", "MALABARISTA", "FOTOGRAFIA", "ESTRATOSFERA", "PALINDROMO", "BUCLE", "VENTANA", "TURBANTE", "KARATE", "CAMARERO", "HOSPITAL", "DIAMANTE", "NINFOMANA", "ANSIEDAD", "VAGABUNDO", "CARAMELO", "TAXIDERMI", "GLOBULO", "ARTESANO", "ENDEMONIADO", "LACRIMOGENO", "UMBRAL", "VIOLIN", "SACAPUNTAS", "SIRENA", "OSCAR", "NEFARIO", "ARMADURA", "PALANCA", "HELICE", "TANGENTE", "CALIZ", "REPLICA", "VOLCAN", "FOSFORO", "PARAPLEJICO", "APATIA", "BUNKER", "EXUDAR", "ANDROIDE", "OBTUSO", "TECLADO", "ESPAÑA", "EUROPA", "AFRICA", "ASIA", "RINOPLASTIA", "HOMOSAPIENS"]
Terminar = False
boleano = True #Creo un boleano que usaré siempre que lo necesite
victoria = 0 #Contador de Victoria
cambiarDificultad = True

while boleano:
    print('¿Tu teclado tiene la letra "Ñ"?') #Preguntamos si el teclado tiene la tecla "Ñ"
    print("1 - SI")
    print("2 - NO")
    letraEspecial = input('Respuesta: ')
    if letraEspecial == "1" or letraEspecial == "2":
        boleano = False
        print("")
    else:
        print("")
        print("Solo respuestas de 1 o 2")
    intentos = 10 #Número de intentos que tienes
#Creo al muñeco que tendrá 5 de altura y 8 de ancho
altura1 = ["", "", "", "", "", "", "", ""]
altura2 = ["", "", "", "", "", "", "", ""]
altura3 = ["", "", "", "", "", "", "", ""]
altura4 = ["", "", "", "", "", "", "", ""]
altura5 = ["", "", "", "", "", "", "", ""]

#La intención es que se vea así
# _____   1
# |    O  2
# |   /|\ 3
# |    |  4
# |   / \ 5
# 12345678 

while cambiarDificultad == True: #Pregunto a ver que opción elije
    print("Escoje tu nivel de dificultad")
    print('1 - dificultad "fácil"')
    print('2 - dificultad "normal"')
    print('3 - dificultad "difícil"')
    preguntar = input("Escoje: ")
    if preguntar == "1":
        dificultad = 1
        cambiarDificultad = False
        continue
    elif preguntar == "2":
        dificultad = 2
        cambiarDificultad = False
    elif preguntar == "3":
        dificultad = 3
        cambiarDificultad = False
    else:
        print("Solo puedes seleccionar 1, 2 o 3")
        print("")
if dificultad == 1: intentos = 10 #Número de intentos que tienes dependiendo el nivel de dificultad
elif dificultad == 2: intentos = 6 #Número de intentos que tienes dependiendo el nivel de dificultad
elif dificultad == 3: intentos = 3 #Número de intentos que tienes dependiendo el nivel de dificultad
while Terminar == False:
    #IMPORTANTE: Todas las variables que estoy creando aquí dentro es porque cada vez que se reinicie el juego, se deberá también reiniciar estas variables
    palabraAcertada = False #Creo una variable para saber si ha acertado la palabra y terminar el juego
    repetirPalabra = True #Comprueba el tamaño de la palabra respecto la dificultad del juego
    muestraPalabra = [] #Para que se muestre los _ en el juego
    letrasUsadas = [] #Para mostrar las letras usadas que estaban erroneas
    accionMenu = "" #Para escojer la acción del menú
    preguntaFin = False #Pregunta al final del juego que quieres hacer

    #Para que se compruebe a ver si tiene "Ñ"
    while repetirPalabra == True:
        palabra = (random.choice(listaPalabras)) #Escojo la palabra aleatoriamente
        rangoPalabra = len(palabra) #Para saber el rango de caracteres de la palabra
        if letraEspecial == "2":
            repetirPalabra = False
            for i in palabra:
                if i == "Ñ":
                    repetirPalabra = True
        elif letraEspecial == "1":
            repetirPalabra = False
        if repetirPalabra == False:
            for i in palabra:
                muestraPalabra += ["_"] #Para añadir los '_' de la palabra
    #Comienzo del juego
    #_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    while palabraAcertada == False:
        boleano = True #Para que siempre que se reinicie el juego, se active como True
        letraAcertada = 0 #Creo una variable que cuenta las letras acertadas en una misma palabra. Ejemplo: Letra que se ingresa (A)
        vuelta = -1 #Creo una variable para contar las iteraciónes que hace al comprobar la palabra y saber la posición donde se ha encontrado
        listaVuelta = [] #Creo la lista para saber las posiciónes
        if intentos == 1: #Creo un if para que el texto esté bien y coincida con el número
            print(f"Tienes {intentos} intento")
        elif intentos == 0:
            print("Intentos acabados, has perdido")
            break
        else:
            print(f"Tienes {intentos} intentos")
        #Recorro la lista y elimino los corchetes, comillas, etc
        print("Palabra secreta: ", end="")
        for i in muestraPalabra:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ") #Hago que se muestre la palabra final
        print("") #Espacio en blanco para saltar el último end que hay
        print("") #Espacio en blanco para un salto de linea completo
        print("Letras erroneas: ", end="")
        for i in letrasUsadas:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ") #Hago que se muestre la palabra final
        print("") #Espacio en blanco para saltar el último end que hay

    #Pregunto la letra y corroboro que sea una letra y no otro caracter
        while boleano: #Mientras sea True
            letra = input("Ingrese un caracter: ")[0:1] #Ingresamos el caracter y obligo al programa a que escoja solo la primera letra que ponemos
            if letra == "": #Si el usuario envia la letra vacía, que la vuelva a pedir
                print("No se permiten parametros vacíos")
                continue
            corroborarLetra = int(ord(letra)) #Calculo si lo que ha ingresado es una letra
            if (corroborarLetra >= 97 and corroborarLetra <= 122) or letra == "ñ": #Si es minuscula o la letra ñ, la convierto en mayuscula y que continúe. Por mas que ponga la letra ñ en ascii, no me lo comprueba bien y me salta error de "solo letras"
                letra = letra.upper()
                boleano = False
            elif (corroborarLetra >= 65 and corroborarLetra <= 90) or letra == "Ñ": #Si es mayuscula o la letra Ñ, que continúe. Por mas que ponga la letra ñ en ascii, no me lo comprueba bien y me salta error de "solo letras"
                boleano = False 
            else: #Si el usuario no me hace caso, que vuelva a pedir los datos
                print("Solo letras sin tildes")
                continue


    #Compruebo si la letra está en la palabra
        for i in palabra:
            vuelta += 1 #Sumo la iteración para saber en que posición de la palabra me encuentro
            if letra == i: #Si la letra introducida coincide con una letra de la palabra
                letraAcertada += 1 #Sumo la letra acertada para saber cuantas letras bien tengo
                listaVuelta += [vuelta] #Apunto las posiciónes donde está la letra en la palabra
            else:
                continue
        if letraAcertada == 0 and letra not in letrasUsadas: #Corroboro que sea una letra que no haya sido acertada ni que ya esté en la lista
            letrasUsadas += [letra] #Apunto la letra usada que no estaba en la palabra (si es que hay)
            intentos -= 1
            #Ahora dibujo al monigote:
            if dificultad == 1:
                if intentos == 9:
                    altura4.pop(0), altura4.insert(0,"|"), altura5.pop(0), altura5.insert(0,"|")
                elif intentos == 8:
                    altura2.pop(0), altura2.insert(0,"|"), altura3.pop(0), altura3.insert(0,"|")
                elif intentos == 7:
                    altura1.pop(0), altura1.insert(0,"_"), altura1.pop(1), altura1.insert(0,"_"), altura1.pop(2), altura1.insert(2,"_"), altura1.pop(3), altura1.insert(1,"_")
                elif intentos == 6:
                    altura2.pop(5), altura2.insert(5,"O")
                elif intentos == 5:
                    altura3.pop(5), altura3.insert(5,"|")
                elif intentos == 4:
                    altura4.pop(5), altura4.insert(5,"|")
                elif intentos == 3:
                    altura3.pop(5), altura3.insert(5,""), altura3.pop(4), altura3.insert(4,"|"), altura3.insert(4,"/"), altura3.pop(3)
                elif intentos == 2:
                    altura3.pop(5), altura3.insert(5,"\\")
                elif intentos == 1:
                    altura5.pop(4), altura5.insert(4,"/")
                elif intentos == 0:
                    altura5.pop(5), altura5.insert(5,"\\")
                else:
                    print("")
                    print("")
                    print(f"Error monigote. El número de intentos es incorrecto: {intentos}")
                    print("")
                    print("")
                    break

            elif dificultad == 2:
                if intentos == 5:
                    altura4.pop(0), altura4.insert(0,"|"), altura5.pop(0), altura5.insert(0,"|"), altura2.pop(0), altura2.insert(0,"|"), altura3.pop(0), altura3.insert(0,"|")
                elif intentos == 4:
                    altura1.pop(0), altura1.insert(0,"_"), altura1.pop(1), altura1.insert(0,"_"), altura1.pop(2), altura1.insert(2,"_"), altura1.pop(3), altura1.insert(1,"_"), altura2.pop(5), altura2.insert(5,"O")
                elif intentos == 3:
                    altura3.pop(5), altura3.insert(5,"|"), altura4.pop(5), altura4.insert(5,"|")
                elif intentos == 2:
                    altura3.pop(5), altura3.insert(5,""), altura3.pop(4), altura3.insert(4,"|"), altura3.insert(4,"/"), altura3.pop(3) 
                elif intentos == 1:
                    altura3.pop(5), altura3.insert(5,"\\"), altura5.pop(4), altura5.insert(4,"/")
                elif intentos == 0:
                    altura5.pop(5), altura5.insert(5,"\\")
                else:
                    print("")
                    print("")
                    print(f"Error monigote. El número de intentos es incorrecto: {intentos}")
                    print("")
                    print("")
                    break

            elif dificultad == 3:
                if intentos == 2:
                    altura4.pop(0), altura4.insert(0,"|"), altura5.pop(0), altura5.insert(0,"|"), altura2.pop(0), altura2.insert(0,"|"), altura3.pop(0), altura3.insert(0,"|"), altura1.pop(0), altura1.insert(0,"_"), altura1.pop(1), altura1.insert(0,"_"), altura1.pop(2), altura1.insert(2,"_"), altura1.pop(3), altura1.insert(1,"_"), altura2.pop(5), altura2.insert(5,"O")
                elif intentos == 1:
                    altura3.pop(5), altura3.insert(5,"|"), altura4.pop(5), altura4.insert(5,"|"), altura3.pop(5), altura3.insert(5,""), altura3.pop(4), altura3.insert(4,"|"), altura3.insert(4,"/"), altura3.pop(3), altura3.pop(5), altura3.insert(5,"\\"), altura5.pop(4), altura5.insert(4,"/")
                elif intentos == 0:
                    altura5.pop(5), altura5.insert(5,"\\")
                else:
                    print("")
                    print("")
                    print(f"Error monigote. El número de intentos es incorrecto: {intentos}")
                    print("")
                    print("")
                    break

        for i in altura1:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ")
        print("")
        for i in altura2:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ")
        print("")
        for i in altura3:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ")
        print("")
        for i in altura4:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ")
        print("")
        for i in altura5:
            if i != "[" and i != "]" and i != "'":
                print(i,end=" ")
        print("")

        if letraAcertada > 0: #Este if es solo para ahorrar calculos a la CPU, si lo quitase no pasaría nada
            for i in range(letraAcertada): #Elimino la posición de la letra acertada y la añado en el mismo lugar con la letra bien puesta
                muestraPalabra.pop(listaVuelta[i])
                muestraPalabra.insert(listaVuelta[i],letra)
        
        if "_" not in muestraPalabra: #Compruebo si la palabra se ha encontrado o no
            palabraAcertada = True
            print("")
            print("Palabra secreta: ", end="")
            for i in muestraPalabra:
                if i != "[" and i != "]" and i != "'":
                    print(i,end=" ") #Hago que se muestre la palabra final completa
            print("")
            print("")

    #Acabo el juego
    #_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    if palabraAcertada == True:
        print("¡Felicidades! Has logrado encontrar la palabra secreta ^·^")
        victoria += 1
    else:
        print(f"La palabra secreta era: {palabra}")
        Terminar = True

    if victoria == 3:
        Terminar = True