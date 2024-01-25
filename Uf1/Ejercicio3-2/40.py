#Llegir tres nombres que denoten una data (dia, mes, any). Comprovar que és una data vàlida. 
#Si no és vàlida dona un missatge d'error. Si és vàlida escriure la data canviant el número del mes pel seu nom.
dia = int(input("Dime el día: "))
mes = int(input("Dime el mes: "))
año = int(input("Dime el año: "))
caja = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
if año % 4==0 and año % 100 !=0 or año % 400 ==0:
    caja[2] = 29

if caja[mes] >= dia and dia >= 1 and mes>0 and mes<=12:
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes = meses[mes]
    print(f"Es correcto, es el {dia} / {mes} / {año}")
else:
    print("No es correcto")