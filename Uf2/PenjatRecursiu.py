paraula_secreta = "python"
lletres_encertades = []
intents_restants = 6

def jugar_penjat(a, b, c):
    letra = input("Dime una letra: ")
    corregir(letra)
    print(f"Intentos: {c}")
    print(b)

    if len(lletres_encertades) == len(paraula_secreta):
        return f"Has encertado la palabra en {intents_restants - c} intentos"
    elif c == 0:
        return f"La palabra secreta era {a} y has agotado todos los intentos. Has adivinado {len(b)} letras"
    else:
        return jugar_penjat(a, b, c-1)

def corregir(a):
    if a not in lletres_encertades:
        for i in paraula_secreta:
            if a == i:
                lletres_encertades.append(a)

resultat = jugar_penjat(paraula_secreta, lletres_encertades, intents_restants)
print(resultat)