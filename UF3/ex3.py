import os, json
def afegirEmpleat():
    global empleats
    try: len(empleats)
    except NameError: empleats = [[" " for i in range(3)] for i in range(1)]
    else: empleats.append([[] for i in range(3)])
    finally:
        while True:
            nom = input("¿Que nombre tiene?\n")
            nom_vacio = nom.replace(" ", "")
            if len(nom_vacio) == 0: print("Tienes que escribir algo")
            else: 
                try: int(nom)
                except ValueError: break
                else: print("El nombre no pueden ser números")
        empleats[len(empleats)-1][0] = nom

        while True:
            try:
                while True:
                    dni = int(input("¿Cual es su DNI?\n"))
                    if len(str(dni)) != 8: print("Tiene que tener una longitud de 8 números")
                    else: break
            except ValueError: print("Solo números, no pongas ninguna letra")
            else:
                dni = str(dni) + letraDNI(dni)
                break
        empleats[len(empleats)-1][1] = dni

        while True:
            try:
                while True:
                    edad = int(input("¿Cuantos años tiene?\n"))
                    if edad > 115: print("No puede tener tantos años")
                    else: break
            except ValueError: print("Solo números, no pongas ninguna letra")
            else: break
        empleats[len(empleats)-1][2] = edad

def letraDNI(numero_dni):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    indice = int(numero_dni) % 23
    return letras[indice]

def mostrar():
    try: len(empleats)
    except NameError: afegirEmpleat()
    else:
        for i in range(len(empleats)):
            for j in range(len(empleats[0])):
                if j == len(empleats[0])-1:
                    print(empleats[i][j])
                else:
                    print(empleats[i][j], end=", ")
            print()

def mostrarJSON():
    directorioActual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directorioActual)
    try:
        with open(filename) as archivo:
            contenido = archivo.read()
            if contenido:
                mostrar = json.loads(contenido)
                print(mostrar)
            else:
                print("El archivo está vacío.")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {filename}.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo {filename} no contiene datos JSON válidos.")

def exportar():
    directorioActual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directorioActual)

    with open(filename, 'w') as f_obj:
        json.dump(empleats, f_obj)

def importar():
    global empleats
    directorioActual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directorioActual)

    try:
        with open(filename) as archivo:
            empleats = json.load(archivo)
            print("Contenido del archivo JSON cargado correctamente:")
            print(empleats)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {filename}.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo {filename} no contiene datos JSON válidos.")

filename = 'trabajadores.json'

while True:
    print("1 - Añadir empleado")
    print("2 - Mostrar empleados (local)")
    print("3 - Exportar empleados")
    print("4 - Mostrar empleados (archivo)")
    print("5 - Importar empleados")
    print("6 - Salir")
    accion = input("¿Que quieres hacer?\n")
    if accion == "1": afegirEmpleat()
    elif accion == "2": mostrar()
    elif accion == "3": 
        while True:
            accion = input("¿Seguro que quieres exportar?\nEsto hará que se borren los datos del archivo y los cambiará por los locales\n1 - Si 2 - No")
            if accion == "1": 
                exportar()
                break
            elif accion == "2": break
            else: print("No has seleccionado ninguna opción correcta")
    elif accion == "4": mostrarJSON()
    elif accion == "5":
        while True:
                accion = input("¿Seguro que quieres importar?\nEsto hará que se borren los datos locales y los cambiará por los del archivo\n1 - Si 2 - No")
                if accion == "1": 
                    importar()
                    break
                elif accion == "2": break
                else: print("No has seleccionado ninguna opción correcta")
    elif accion == "6":
        print("¡Ha sido un placer!")
        break
    else: print("ERROR: No has escogido una opción válida")
