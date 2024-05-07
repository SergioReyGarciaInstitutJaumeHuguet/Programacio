#Crea un programa que vagi demanant a l'usuari introduir números per teclat fins a introduir el número 0. 
#Cada número introduït s'afegirà a una llista. Un cop introduïts tots els números, es mostrarà per pantalla  
#tots ells en una única línia, així com la suma de tots ells en una altra línia i la quantitat de números 
#introduïts en una altra. S'haurà de validar que l'usuari no introdueixi caràcters no numèrics.

lista = []
suma = 0
while True:
    x = input("Dime números aleatorios, para terminar escribe 0: ")
    if x == "0":
        break
    if x.isdigit():
        x = int(x)
        lista += [x]
    else:
        print("Error")
for i in lista:
    suma += i
print(lista)
print("La suma de todos los números son ", suma)
print("La longitud de la lista es de ", len(lista))