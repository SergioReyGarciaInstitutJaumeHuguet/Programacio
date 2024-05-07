#Crear un programa amb Python que donar un vector de 10 posicions faci l'invers de l'anterior exercici 
lista = [1,2,3,4,5,6,7,8,9,10]
ultnum = lista[0]
for i in range(0, len(lista)-1):
    lista[i] = lista[i+1]
lista[-1] = ultnum
print(lista)