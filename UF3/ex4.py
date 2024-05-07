import re, os, json

filename = "ex4.json"
ñ = True

def agregarContacte():
    while True:
        nom = input("¿Que nombre tiene?\n")
        nom = name(nom)
        if nom != True: break
    while True:
        telefon = input("¿Cual es su número de teléfono?\n")
        telefon = tlf(telefon)
        if telefon != True: break
    while True:
        mail = input("Cual es su email?\n")
        mail = email(mail)
        if mail != True: break
    while True:
        newsletter = input("¿Tiene Newsletter activado?\n1 - Si\n2 - No\n")
        newsletter = nl(newsletter)
        if newsletter == True or newsletter == False: break
    afegirContacte(contacto = [nom, telefon, mail, newsletter])

def name(x):
    nom_vacio = x.replace(" ", "")
    if len(nom_vacio) == 0: print("Tienes que escribir algo")
    else: 
        try: int(x)
        except ValueError: return x
        else: 
            print("El nombre no pueden ser números")
            return True

def tlf(x):
    telefonVacio = x.replace(" ","").replace("-","").replace("#","").replace("*","")
    if verificar(telefonVacio, "Teléfono") != True: 
        print("El número de teléfono ya está registrado")
        return True
    else:
        try: int(telefonVacio)
        except ValueError: 
            print("El número no puede contener letras y si está separado, tiene que ser por espacios o guiónes como estos '-'")
            return True
        else: return x

def email(x):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,x)): return(x)
    else: 
        print("No es un correo válido")
        return True

def nl(x):
    if x != "1" and x != "2": 
        print("No es una opción válida")
        return "Error"
    elif x == "1": 
        x = True
        return x
    else: 
        x = False
        return x

def afegirContacte(contacto):
    global agenda, id
    cosas = ["ID","Nombre", "Teléfono", "Email", "Newsletter"]
    try: id += 1
    except TypeError: id = 1
    finally:
        try: len(agenda)
        except NameError: 
            agenda = []
    cosa = {}
    for i in range(len(cosas)):
        if i == 0: cosa[cosas[i]] = id
        else: cosa[cosas[i]] = contacto[i-1]
    agenda.append(cosa)

def mostrarContactes():
    try: len(agenda)
    except NameError: 
        print("No hay ningún contacto")
        return True
    else: 
        print("CONTACTOS")
        for contacto in agenda: 
            for k,v in contacto.items():
                if k == "Newsletter":
                    if v == True: v = "Si"
                    else: v = "No"
                print(f"{k}: {v}", end=" ")
            print()

def verificar(x,y):
    try: len(agenda)
    except NameError: return True
    else:
        for i in range(len(agenda)):
            b = agenda[i]
            try: b[y]
            except KeyError: pass
            else:
                if b[y] == x: 
                    return False
        else: return True

def modificarContacte():
    lista = ["Nombre: ", "Teléfono: ", "Email: ", "Newsletter: "]
    if mostrarContactes(): pass
    else:
        try: id = int(input("Dime el id de la persona que quieres modificar: "))
        except ValueError: print("Tiene que ser un número válido")
        else:
            if verificar(id, "ID") != False:
                for i in range(len(lista)):
                    if i == 3: print("1 - Si\n2 - No\n")
                    accion = input(f"{lista[i]}")
                    if accion != "":
                        a = agenda[id-1]
                        if i == 0: a["Nombre"] = name(accion)
                        elif i == 1: a["Teléfono"] = tlf(accion)
                        elif i == 2: a["Email"] = email(accion)
                        elif i == 3: a["Newsletter"] = nl(accion)
                        else: print("ERROR")

def cercarContacte():
    while True:
        nom = input("Dime un nombre\n")
        name(nom)
        if name != True: break
    if verificar(nom, "Nombre") != True: mostrarContacte(nom)
    else: print("No tienes ningún usuario registrado de esa forma")

def mostrarContacte(x):
    try: len(agenda)
    except NameError: 
        print("No hay ningún contacto")
        return True
    else: 
        for i in range(len(agenda)):
            b = agenda[i]
            try: b["Nombre"]
            except KeyError: pass
            else:
                if b["Nombre"] == x: 
                    print(agenda[i])

def exportar():
    directorioActual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directorioActual)

    with open(filename, 'w') as f_obj:
        json.dump(agenda, f_obj)

def importar():
    global agenda, id
    directorioActual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(directorioActual)

    try:
        with open(filename) as archivo:
            agenda = json.load(archivo)
            print("Contenido del archivo JSON cargado correctamente:")
            mostrarContactes()
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {filename}.")
    except json.decoder.JSONDecodeError:
        print(f"El archivo {filename} no contiene datos JSON válidos.")
    id = agenda[-1]["ID"]

def eliminarContacte():
    mostrarContactes()
    try: id = int(input("Dime el id de la persona que quieres eliminar\n"))
    except ValueError: print("Solo números")
    else:
        if verificar(id,"ID") == False: del agenda[id-1]
        

def menu():
    while True:
        print("AGENDA")
        print("1 - Afegir contacte")
        print("2 - Mostrar Agenda")
        print("3 - Buscar contacte")
        print("4 - Modificar contacte")
        print("5 - Esborrar contacte")
        print("6 - Exportar contacte")
        print("7 - Importar contacte")
        print("8 - Salir")
        accion = input("Selecciona una opción\n")
        if accion == "1": agregarContacte()
        elif accion == "2": mostrarContactes()
        elif accion == "3": mostrarContacte()
        elif accion == "4": modificarContacte()
        elif accion == "5": eliminarContacte()
        elif accion == "6": exportar()
        elif accion == "7": importar()
        elif accion == "8": break
        else: print("No es una opción válida")

menu()