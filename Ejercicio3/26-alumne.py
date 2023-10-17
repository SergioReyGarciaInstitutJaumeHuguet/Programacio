#Calcular les qualificacions d'un grup d'alumnes. La nota final de cada alumne es calcula seguint el criteri: 
#la part pràctica val el 10%; la part de problemes val un 50% i la part teòrica el 40%. 
#Llegirà tres notes de cada alumne fins trobar les tres notes com a 0. 
#Les notes han d'estar entre 1 i 10, si no ho estan, no imprimirà les notes, donarà error i llegirà les d'un altre alumne.
x = True
y = 0
nota1 = 0
nota2 = 0
nota3 = 0
while x == True:
    alumno = input("Nombre del alumno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    if nota1 == 0 and nota2 == 0 and nota3 == 0:
        print("Todo es un 0")
        x = False
        continue
    elif nota1 > 10 or nota2 > 10 or nota3 > 10:
        print("Error, algún número es mayor a 10")
        continue
    else:
        nota1 = nota1 * 0.1
        nota2 = nota2 * 0.5
        nota3 = nota3 * 0.4
        y = nota1 + nota2 + nota3
    print(f"El alumno {alumno} tiene una media de {y}")