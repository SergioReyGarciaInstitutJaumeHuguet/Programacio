#L'associació de vinicultors té com a política fixar un preu inicial a el quilo de raïm, 
#la qual es classifica en tipus A i B, i més en mides 1 i 2. 
#Quan es realitza la venda del producte, aquesta és d'un sol tipus i grandària , es requereix determinar quant rebrà un 
#productor pel raïm que lliura en un embarcament, considerant el següent: 
#si és de tipus a, se li carreguen 20 cèntims a el preu inicial quan és de mida 1; i 30 cèntims si és de mida 2. 
#Si és de tipus B, es rebaixen 30 cèntims quan és de mida 1, i 50 cèntims quan és de grandària 2. 
#Feu un algoritme per determinar el guany obtingut.

preuK = float(input("Dime el precio del kilo de racimos: "))
aob = input("Es tipo A o B: ")
tam = int(input("Son de tamaño 1 o 2: "))
if aob == "a" or aob == "A" and tam == 1:
    final = preuK + 0.20
    print(f"El precio final será: {final}")
elif aob == "a" or aob == "A" and tam == 2:
    final = preuK + 0.20
    print(f"El precio final será: {final}")
elif aob == "b" or aob == "B" and tam == 1:
    final = preuK - 0.30
    print(f"El precio final será: {final}")
elif aob == "b" or aob == "B" and tam == 1:
    final = preuK - 0.50
    print(f"El precio final será: {final}")
else:
    print("El precio es negativo o lo has hecho mal. Tu negocio se va a quiebre.")

print("")
print("¿Cuantos kilos hay?")
kilos = int(input())
print(f"El precio final será {final * kilos}€")