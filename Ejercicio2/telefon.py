#La política de cobrament d'una companyia telefònica és: quan es realitza una trucada, 
#el cobrament és pel temps que aquesta dura, de tal manera que els primers cinc minuts costen 1 euro, 
#els següents 3, 80 cèntims, els següents dos minuts, 70 cèntims, i a partir del desè minut, 50 cèntims.
#A més a més, es carrega un impost de 3% quan és diumenge, i si és un altre dia, en torn de matí, 15%, 
#i en torn de tarda, 10%. Feu un algoritme per determinar quant ha de pagar per cada concepte una persona que realitza una trucada.
dinero = 0
dinero2 = 0
temps = float(input("¿Cuantos minutos ha durado la llamada? "))
horari = float(input("¿A que hora ha sido? (Formato 24H) "))
while horari > 24:
    horari = float(input("¿A que hora ha sido? (Formato 24H) "))
print("¿Que día es?")
print("L = Lunes")
print("M = Martes")
print("X = Miercoles")
print("J = Jueves")
print("V = Viernes")
print("S = Sabado")
print("D = Domingo")
dia = input("Día: ")
while dia != "L" and dia != "M" and dia != "X" and dia != "J" and dia != "V" and dia != "S" and dia != "D" and dia != "l" and dia != "m" and dia != "x" and dia != "j" and dia != "v" and dia != "s" and dia != "d":
    print("Dato no válido, vuelva a ingresarlo")
    dia = input("Día: ")
if temps > 10:
    dinero2 = (5*1) + (3*0.8) + (2*0.7)
    dinero = (temps - 10) * 0.50
elif temps <= 10 and temps > 8:
    dinero2 = (5 * 1) + (3 * 0.8)
    dinero = (temps-8) * 0.7
elif temps <= 8 and temps > 5:
    dinero2 = (5 * 1)
    dinero = (temps-5) * 0.8
else:
    dinero = temps * 1

dinerototal = dinero + dinero2
if dia == "D" or dia == "d":
    dinerototal = (dinerototal*0.3)+dinerototal
if horari <= 12 and dia != "D" or dia != "d":
    dinerototal = (dinerototal * 0.15)+dinerototal
elif horari >= 12 and dia != "D" or dia != "d":
    dinerototal = (dinerototal * 0.1)+dinerototal
print(f"El coste de la llamada será {dinerototal}€")