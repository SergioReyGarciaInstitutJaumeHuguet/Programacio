#Dissenya un algorisme corresponent a un programa que donada una frase acabada en punt, 
#compti el nombre de caràcters que hi apareixen a partir de la primera “a”.
print("Dime una frase que contenga la letra A y termine en .")
x = input("")
z = 0
y = 0
for i in range(len(x)):
    caracter = x[i]
    if caracter == ".":
        y = 1
    if caracter == "a" or caracter == "A":
        z = z+1
if y == 1:
    print(f"Los caracteres con A que hay son: {z}")
elif y == 0:
    print(f"No has terminado la frase con '.', pero los caracteres con A que hay son: {z}")
