no_alum = int(input("Introdueix el nombre d'alumnes: "))

alumnes={}

for alumne in range(no_alum):
    alumne = input("\nIntrodueix el nom de l'alumne: ")
    notes = []
    while True:
        nota_alumne = float(input("\nIntrodueix la nota de l'alumne(-1 per finalitzar): "))
        if nota_alumne < 0:
            break
        notes.append(nota_alumne)

    alumnes[alumne] = notes

print("\nMitjanas:\n")
for i, j in alumnes.items():
    print(f"{i}: {sum(j) / len(j)}")