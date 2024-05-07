#Dissenya un algorisme corresponent a un programa que donada una frase acabada en punt, 
#compti el nombre de caràcters que hi apareixen, sense comptar el punt.
print("Dime una frase que termine en .")
x = input("")
z = 0
y = 1
for i in range(len(x)):
    caracter = x[i]
    z = z+1
    if caracter == ".":
        z -= 1
        print(f"Los caracteres que hay son: {z}")
        y = 0
if y == 1:
    print(f"No has añadido punto final pero tienes {z} caracteres")