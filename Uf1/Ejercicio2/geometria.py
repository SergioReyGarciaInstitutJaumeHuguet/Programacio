#Programa que llegeixi tres dades d'entrada A, B i C. Aquests corresponen a les dimensions dels costats d'un triangle. 
#El programa ha de determinar quin tipus de triangle és, tenint en compte els següent:
#Si es compleix Pitàgores llavors és triangle rectangle
#Si només dos costats de el triangle són iguals llavors és isòsceles.
#Si els 3 costats són iguals llavors és equilàter.
#Si no es compleix cap de les condicions anteriors, és escalè.

a = float(input("Dime el primer tamaño: "))
b = float(input("Dime el segundo tamaño: "))
c = float(input("Dime el tercer tamaño: "))
res = pow(pow(a,2) + pow(b,2),0.5)
if c == res:
    print("Es un rectangle")
elif a==b and b==c:
    print("El triangle es equilàter")
elif a == b:
    print("El triangle es isòceles")
else:
    print("Es escalè")