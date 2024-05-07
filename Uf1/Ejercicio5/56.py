#Demanem 10 valors a l'usuari i els emmagatzemem en un vector de 10 posicions. 
#Seguidament demanem un valor a l'usuari que buscarem dins el vector. 
#Finalment mostrarem per pantalla en quina posició l'hem guardat, si no el troba li diem que no hi és.
y = False
z = -1
lista = []
for i in range(10):
    x = input("Dime valores: ")
    lista += [x]
x = input("Corroboremos si el valor está: ")
for i in lista:
    z += 1
    if x == i:
        y = True
        break
if y == True:
    print(f"El dato está en la lista. Está en la posición {z}") # Recordemos que la posición comienza en 0
else:
    print("El dato no está en la lista.")