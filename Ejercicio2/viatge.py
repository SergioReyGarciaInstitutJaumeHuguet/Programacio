#El director d'una escola està organitzant un viatge d'estudis, i requereix determinar quant ha de cobrar a cada alumne 
#i quant ha de pagar a la companyia de viatges pel servei. 
#La manera de cobrar és la següent: si són 100 alumnes o més, el cost per cada alumne és de 65 euros; 
#de 50 a 99 alumnes, el cost és de 70 euros, de 30 a 49, de 95 euros, 
#i si són menys de 30, el cost de la renda de l'autobús és de 4000 euros, sense importar el nombre d'alumnes.
#Feu un algoritme que permeti determinar el pagament a la companyia d'autobusos i el que ha de pagar cada alumne pel viatge.

alumnes = int(input("¿Cuantos alumnos son? "))
if alumnes >= 100:
    preu = alumnes * 65
elif alumnes >= 50 and alumnes <= 99:
    preu = alumnes * 70
elif alumnes >= 30 and alumnes <= 49:
    preu = alumnes * 95
else:
    preu = alumnes / 4000

print(f"El precio total será {preu}€")

