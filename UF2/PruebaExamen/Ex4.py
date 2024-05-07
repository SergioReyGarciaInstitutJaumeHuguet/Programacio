estudiants = []
def afegir():
    global estudiants
    nom = input("El nom del estudiant\n")
    while True:
        edat = input("L'edat del estudiant\n")
        if edat.isnumeric():
            edat = int(edat)
            if edat >= 16 and edat <= 100: break
            else: print("Solo números del 16 al 100")
        else: print("Nomes números")
    while True:
        nota = input("Nota de l'estudiant\n")
        a = nota.replace(".", "")
        if a.isnumeric(): 
            nota = float(nota)
            if nota >= 0 and nota <= 10: break
            else: print("Solo números del 0 al 10")
        else: print("Nomes números")
    estudiants.append({
        "Nom": nom,
        "Edat": edat,
        "Nota": nota
    })

def ver():
    a = 0
    accion = input("Que quieres hacer\n1 - Ver a todos los alumnos\n2 - Ver a los alumnos mayores de 20 años\n")
    if accion == "1":
        for i in range(len(estudiants)):
            for j in estudiants[i]:
                print(f"{j}: {estudiants[i][j]}")
    elif accion == "2":
        for i in range(len(estudiants)):
            if estudiants[i]["Edat"] > 20:
                a += 1
                for j in estudiants[i]:
                    print(f"{j}: {estudiants[i][j]}")
                print()
        if a == 0: print("No hay ningún alumno mayor de 20 años")
        else: a = 0

while True:
    accion = input("Que quieres hacer\n1 - Añadir alumno\n2 - Ver alumnos\n3 - salir\n")
    if accion == "1": afegir()
    elif accion == "2": 
        if len(estudiants) > 0:
            ver()
        else: print("No hay ningún alumno en la lista")
    elif accion == "3": break
    else: print("Debes escojer algún número")
