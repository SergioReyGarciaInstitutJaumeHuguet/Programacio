import os

direcotrioActual = os.path.dirname(os.path.abspath(__file__)) # Guarda la ubicación del archivo
os.chdir(direcotrioActual) # Se mueve a la ubicación del archivo

filename = 'noms.txt' # Nombre del fichero

with open(filename, 'w') as escribir:
    pass # Para vaciar

with open(filename, 'a') as añadir: # Pide el nombre para añadirlo al .txt
    for i in range(5):
        nombre = input(f"Dime el nombre {i+1}: ")
        añadir.write(f"{nombre}\n")

with open(filename, 'r') as letras: # Lee el archivo
    contents = letras.read()
print(contents)
