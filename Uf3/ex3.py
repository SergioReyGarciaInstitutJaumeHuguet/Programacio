def afegirEmpleat():
    global empleats
    try:
        len(empleats)
    except NameError:
        empleats = [[" " for i in range(3)] for i in range(1)]
    else:
        empleats.append([[] for i in range(3)])
    finally:
        while True:
            nom = input("¿Que nombre tiene?\n")
            nom_vacio = nom.replace(" ", "")
            if len(nom_vacio) == 0: print("Tienes que escribir algo")
            else: 
                try:
                    int(nom)
                except ValueError:
                    break
                else:
                    print("El nombre no pueden ser números")
        empleats[len(empleats)-1][0] = nom
        while True:
            try:
                while True:
                    dni = int(input("¿Cual es su DNI?\n"))
                    if len(str(dni)) != 8: print("Tiene que tener una longitud de 8 números")
                    else: break
            except ValueError:
                print("Solo números, no pongas ninguna letra")
            else:
                dni = str(dni) + letraDNI(dni)
                break
        empleats[len(empleats)-1][1] = dni

def letraDNI(numero_dni):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    indice = int(numero_dni) % 23
    return letras[indice]

afegirEmpleat()
print(empleats)