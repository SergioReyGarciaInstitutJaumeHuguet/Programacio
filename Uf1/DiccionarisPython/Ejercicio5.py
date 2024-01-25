agenda={}

while True:
    print("__\n\n1. Afegir/ modificar contacte")
    print("2. Cercar contactes")
    print("3. Llistar contactes")
    print("4. Eliminar contacte")
    print("5. Sortir")
    opc=int(input("\n__\n\nTria una opció: "))

    if opc==1:
        nom=input("\nIntrodueix el nom: ")
        if nom in agenda.keys():
            print(f"Ja tens aquest contacte\n{nom}: {agenda[nom]}")
            modificar=input("\nVols canviar el telf? (s/n)")
            if modificar=="s":
                telf=int(input("Introdueix el telf: "))
                agenda[nom]=telf
            else:
                continue
        else:
            telf=int(input("Introdueix el telf: "))
            agenda[nom]=telf
    elif opc==2:
        letra=input("\nIntrodueix el/s caracters: ")
        for nom in agenda.keys():
            if nom.startswith(letra):
                print(f"Contactes que començen per {letra}\n{nom}: {agenda[nom]}\n")
            else:
                print(f"No hi ha contactes que començin per {letra}\n")
    elif opc==3:
        for nom in agenda.keys():
            print(f"{nom}: {agenda[nom]}")
    elif opc==4:
        nom=input("Introdueix el nom: ")
        if nom in agenda.keys():
            del agenda[nom]
        else:
            print("No hi ha aquest contacte")
    elif opc==5:
        break
