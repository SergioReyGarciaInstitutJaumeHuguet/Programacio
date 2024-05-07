print("¡ATENCIÓN!")
print("El abecedario es Español, es decir, se incluye ñ y no se usa la ç")
print("Las letras se tienen que poner en minuscula o dará error")
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vuelta = 1
letra = 0
porcentaje = 0
for i in range(13):
    letra = input(f"Que letra hay entre: {abecedario[vuelta-1]} - {abecedario[vuelta+1]}\n")
    if letra == abecedario[vuelta]:
        print("¡Correcto!")
        porcentaje += 1
    else:
        print("Incorrecto")
    vuelta += 2
porcentaje = (porcentaje/13)*100
if porcentaje > 80:
    print(f"Has ganado con un {porcentaje}% de encertados")
else:
    print(f"Has perdido con un {porcentaje}% de encertados")