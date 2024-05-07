#Crear un programa amb Python que donat un vector de 10 posicions passi tots els valors a 
#la posició de la dreta. 
#El valor de la última casella passarà a la primera casella del vector.

lista = [1,2,3,4,5,6,7,8,9,10]
ultnum = lista[-1]
for i in range(len(lista)-2, -1, -1):
    lista[i+1] = lista[i]
lista[0] = ultnum
print(lista)