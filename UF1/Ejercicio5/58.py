ytuygihojuj = '''Fer un programa que demani per teclat les següents dades

*  Els ingressos que Joan ha rebut durant els dotze mesos de l'any.

*  La quantitat a cercar a dintre del vector.

Com a resultat de la cerca el programa ens ha de dir si Joan ha rebut o no aquesta quantitat, 
i en cas positiu, ens digui en quin mes l'ha cobrat (gener, febrer, ...).'''
lista = []
a = -2
x = False
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for i in range(0,12):
    ingresos = input(f"¿Cuanto dinero ha obtenido el Joan el mes de {mes[i]}? ")
    lista += [ingresos]
buscar = input("¿Dime la cantidad que haya recibido algún mes? ")
for i in lista:
    a += 1
    if buscar == i:
        x = True
        break
if x == True:
    print(f"El mes que ha cobrado eso ha sido en {mes[a]}")
else:
    print("No ha cobrado eso en ningún mes")