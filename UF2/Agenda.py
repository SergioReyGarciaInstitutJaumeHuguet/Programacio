agenda = {}

def agregar_contacto():
    global agenda
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = int(input("Ingresa el teléfono del contacto: "))
    while telefono in agenda:
        print("Este número de teléfono ya existe.")
        telefono = int(input("Ingresa el teléfono del contacto: "))
    edad = int(input("Ingresa la edad del contacto: "))
    agenda[telefono] = {'nombre': nombre, 'telefono': telefono, 'edad': edad}

def mostrar_contactos():
    global agenda
    for contacto in agenda.values():
        print(f"Nombre: {contacto['nombre']}\nEdad: {contacto['edad']} años \nTeléfono: {contacto['telefono']}.")

def mayores_de_20():
    global agenda
    for contacto in agenda.values():
        if contacto['edad'] >= 20:
            print(f"Nombre: {contacto['nombre']}\nEdad: {contacto['edad']} años \nTeléfono: {contacto['telefono']}.")

def menu_principal():
    print("-------------")
    print("AGENDA")
    print("-------------") 
    print("1. Agregar contactos")
    print("2. Mostrar contactos")
    print("3. Mostrar contactos mayores de 20 años")
    print("4. Salir")

while True:
    menu_principal()
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        mostrar_contactos()
    elif opcion == 3:
        mayores_de_20()
    elif opcion == 4:
        break
    elif opcion < 1 or opcion > 4:
        print("¡Error!")
