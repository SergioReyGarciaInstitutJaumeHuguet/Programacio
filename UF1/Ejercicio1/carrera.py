coche1 = int(input("Dime a cuanta velocidad va el primer coche: "))
coche2 = int(input("Dime a cuanta velocidad va el segundo coche: "))
distancia = float(input("Dime la distancia en kilometros de la que se separan: "))
a = coche1-coche2
v = distancia/a
res = v*60
print(f"Tardará {res} minutos.")