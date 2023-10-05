# Algorisme que demani dos nombres 'nota' i 'edat' i un caràcter 'sexe' i mostri el missatge 'ACCEPTADA' 
# si la nota és major o igual a cinc, l'edat és més gran o igual a divuit i el sexe és 'F'. 
# En cas que es compleixi el mateix, però el sexe sigui 'M', ha imprimir 'POSSIBLE'. 
# Si no es compleixen aquestes condicions s'ha de mostrar 'NO ACCEPTADA'.

nota = float(input("Dime la nota: "))
edad = int(input("Dime la edad: "))
sexo = input("Dime F si eres mujer o M si eres hombre: ")
if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("ACCEPTADA")
    else:
        print("POSSIBLE")
else:
    print("NO ACCEPTARA")