dia = int(input("Dime el día: "))
mes = int(input("Dime el mes: "))
año = int(input("Dime el año: "))
caja = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
if año % 4==0 and año % 100 !=0 or año % 400 ==0:
    caja[2] = 29

if caja[mes] >= dia and dia >= 1 and mes>0 and mes<=12:
    print(f"Está correcto, es el {dia}/{mes}/{año}")
else:
    print("No es correcto")