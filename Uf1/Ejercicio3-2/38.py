#Tenint en compte que la clau és "eureka", escriure un algorisme que ens demani una clau. 
#Únicament tenim 3 intents per encertar, si fallem els 3 intents ens mostrarà un missatge 
#indicant-nos que hem esgotat els intents. Si encertem la clau, sortirem directament.
z = 3
print((f"Dime la clave, tienes {z} intentos"))
for i in range(3):
    x = input("")
    if x == "eureka":
        print("Felicidades")
        break
    elif z != "eureka":
        z -= 1
        if z > 1:
            print(f"Mal hecho, te quedan {z} intentos")
        else:
            print(f"Mal hecho, te queda {z} intento")
    if z == 0:
        print("Intentos terminados")