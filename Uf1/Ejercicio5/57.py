#Programa que demani les dates de naixement de 20 alumnes de la classe i ens digui qui és l'alumne més jove 
#i el més vell. Dels dos alumnes resultants, ens haurà de dir si son del mateix any. Les dates de naixement 
#dels alumnes emmagatzemades a un vector hauran de tenir el format aaaa/mm/dd, on aaaa és l'any, mm el més i
#dd el dia de naixement.

lista = ["1995/12/25", "2005/04/21", "1914/06/18"]
menor = max(lista).split("/")[0]
mayor = min(lista).split("/")
print(mayor)
if mayor == menor:
    print("Son del mismo año")
else:
    print("No son del mismo año")