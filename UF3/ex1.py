# Exercici 1
try:
    resultat= 10/0
    print(resultat)
except ZeroDivisionError:
    print("No se puede dividir por 0")

# Exercici 2
llista = [1, 2, 3, 4, 5]
try:
    llista[10]
except IndexError:
    print("No existe la decima posición en la lista")

# Exercici 3
colors = { 'vermell':'red', 'verd':'green', 'negre':'black ' } 

try:
    colors['blanc']
except KeyError:
    print("No existe el color 'blanc' en el diccionario")

# Exercici 4
try:
    resultat = 15 + "20"
except TypeError:
    print("No se puede sumar un entero con un string")

# Exercici 5
def afegirUnic(elem):
    global lista
    if elem in lista:
        raise ValueError(f"No se pueden añadir valores duplicados: {elem}")
    else:
        lista.append(elem)

lista = [1, 5, -2]

try:
    afegirUnic(10)
    afegirUnic(-2)
    afegirUnic("Hola")
except ValueError as e:
    print(e)

print(lista)
