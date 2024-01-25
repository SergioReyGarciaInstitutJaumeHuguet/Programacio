liherjgnouwjklgtnog = '''Demanem per teclat un llistat d'assignatures i les seves respectives notes 
( en una altra llista). Al final del programa mostrarem la assignatura amb la seva respectiva nota. 
Es valorarà que s'alterni la introducció de les assignatures amb les notes.'''

asignatures = []
nota = []
x = True
a = -1
while x:
    asig = input("Dime asignaturas, si quieres parar escribe 0: ")
    if asig == "0":
        x = False
        continue
    asignatures.append(asig)
for i in asignatures:
    a += 1
    notaM = int(input(f"Dime la nota de {asignatures[a]}: "))
    nota.append(notaM)
nota = sum(nota)
media = nota/(a+1)
print(f"La nota media es un {media}")