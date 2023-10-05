base = float(input("Dime el sueldo base: "))
ven1 = float(input("Dime el dinero de la venta 1: "))
ven2 = float(input("Dime el dinero de la venta 2: "))
ven3 = float(input("Dime el dinero de la venta 3: "))
vent1 = (ven1*10)/100
vent2 = (ven2*10)/100
vent3 = (ven3*10)/100
res = (base+ven1+ven2+ven3+vent1+vent2+vent3)
print(f"El resultado es {res}")