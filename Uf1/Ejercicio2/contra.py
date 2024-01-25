#Escriu un programa que demani un nom d'usuari i una contrasenya i si s'ha introduït "anna" i "12345" s'indica "Has entrat a sistema", sinó es dona un error.
usuari = input("Nombre: ")
contra = input("Contraseña: ")
if usuari == "anna" and contra == "12345":
    print("Sesión iniciada")
else:
    print("Sesió incorrecta")
