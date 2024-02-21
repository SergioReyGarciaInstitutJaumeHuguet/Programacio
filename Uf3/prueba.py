import json
import os

# Obtener la ubicación del archivo actual
directorioActual = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorioActual)  # Cambiar al directorio actual

numbers = [["Sergio", "77791827P", 18]]
filename = 'noms.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

try:
    with open(filename) as archivo:
        contenido = archivo.read()
        if contenido:
            numeros = json.loads(contenido)
            print(numeros)
        else:
            print("El archivo está vacío.")
except FileNotFoundError:
    print(f"No se pudo encontrar el archivo {filename}.")
except json.decoder.JSONDecodeError:
    print(f"El archivo {filename} no contiene datos JSON válidos.")