import random
listaPalabras = ["CIELO", "ENSALADA", "SUEÑO", "LIBRO", "MUSICA", "VIDA", "MUERTE", "LUZ", "OSCURIDAD", "ESPERANZA", "DESESPERACION", "CALOR", "FRIO", "SABOR", "OLOR", "SILENCIO", "RUIDO", "PENSAMIENTO", "ACCION", "PALABRA", "IMAGINACION", "FANTASIA", "REALIDAD", "CREACION", "DESTRUCCION", "PASADO", "FUTURO", "AHORA", "SIEMPRE", "NUNCA", "CORAZON", "MENTE", "ALMA", "CUERPO", "FAMILIA", "AMISTAD", "AMBIENTE", "CIRCUNSTANCIA", "PROBLEMA", "SOLUCION", "DESTINO", "CAMINO", "SECRETO", "AVENTURA", "DESCUBRIMIENTO", "CONOCIMIENTO", "IGNORANCIA", "BONDAD", "MALDAD", "PAZ", "GUERRA", "ARTE", "CIENCIA", "TECNOLOGIA", "NATURALEZA", "CIUDAD", "CAMPO", "OCEANO", "MONTAÑA", "DESERTO", "BOSQUE", "ANIMAL", "PLANTA", "HOMBRE", "MUJER", "NIÑO", "ADULTO", "JOVEN", "VIEJO", "RICO", "POBRE", "GRANDE", "PEQUENO", "LARGO", "CORTO", "RAPIDO", "LENTO", "ALTO", "BAJO", "ROTO", "ENTERO", "DIFICIL", "FACIL", "FELICIDAD", "TRISTEZA", "ENFADO", "AMOR", "ODIO", "MIEDO", "VALOR", "DUDA", "CONFIANZA", "SORPRESA", "ABURRIMIENTO", "CABEZA", "JAUME", "MARIA", "IZAN", "ESPAÑA", "ARBOL", "MARIPOSA", "COMPUTADORA", "CATEDRAL", "ELEFANTE", "PIJAMA", "KIWI", "PELOTA", "HEROE", "BARCO", "TREN", "MANZANA", "GORILA", "CEBRA", "LORO", "LEON", "TIGRE", "JAGUAR", "COCODRILO", "ELECCION", "HORMIGA", "AGUILA", "HALCON", "CALABAZA", "CEBOLLA", "CANGREJO", "CABALLO", "FRESA", "GATO", "PERRO", "CUCHILLO", "MAR", "RANA", "NUBE", "BICICLETA", "LAPIZ", "HORMIGON", "RATON", "LLAVE", "CAMARA", "GUITARRA", "PAJARO", "LINTERNA", "SILLA", "RELOJ", "AGUACATE", "ESMERALDA", "TELESCOPIO", "ESCORPION", "JARDINERO", "PLATILLO", "CIRCUNFERENCIA", "RINOCERONTE", "ELECTRICIDAD", "ENIGMA", "RUBI", "OXIGENO", "SINFONIA", "GUSANO", "MAJESTUOSO", "CAMELLO", "DOMINO", "CAMALEON", "RELOJERIA", "VINAGRE", "YOGUR", "TORNADO", "PAISAJE", "TIBURON", "PENDULO", "JUBILACION", "CACAHUETE", "MISTERIO", "CARBON", "CUARTEL", "AMAPOLA", "NAVEGAR", "ACROBATA", "CACTUS", "XILOFONO", "PERSIANA", "EXOTICO", "MALABARISTA", "FOTOGRAFIA", "BUCLE", "VENTANA", "CAMARERO", "HOSPITAL", "DIAMANTE", "ANSIEDAD", "VAGABUNDO", "CARAMELO", "ARTESANO", "VIOLIN", "SACAPUNTAS", "SIRENA", "OSCAR", "ARMADURA", "PALANCA", "HELICE", "TANGENTE", "CALIZ", "REPLICA", "VOLCAN", "FOSFORO", "BUNKER", "EXUDAR", "ANDROIDE", "OBTUSO", "TECLADO", "EUROPA", "AFRICA", "ASIA", "HOMOSAPIENS"]
palabra = (random.choice(listaPalabras))
rangoPalabra = int(len(palabra))
lista = []
listaAux = []

for i in palabra:
    lista.append(i)
    listaAux.append(i)

x = 0
for i in lista:
    if i == "Ñ":
        x += 1
    elif i == "K":
        x += 1
    elif i == "Q":
        x += 1
    elif i == "W":
        x += 1
    elif i == "X":
        x += 1
    elif i == "Y":
        x += 1
    elif i == "Z":
        x += 1
    elif i == "F":
        x += 1
    elif i == "J":
        x += 1
    elif i == "P":
        x += 1

if x > 5:
    x /= 2
for x in range(int(((rangoPalabra/2)-1)+x)):
    listaAux = []
    for i in lista:
        listaAux.append(i)
    derechaIz = 1 #Restar de dos en dos de derecha a izquierda
    izquierdaDe = -1 #Sumar uno en uno de izquierda a derecha
    for i in range(rangoPalabra):
        derechaIz -= 2
        izquierdaDe += 1
        if derechaIz < (rangoPalabra*-1):
            derechaIz = -2
        lista[derechaIz] = listaAux[izquierdaDe]


print(lista)
input("")
print(palabra)