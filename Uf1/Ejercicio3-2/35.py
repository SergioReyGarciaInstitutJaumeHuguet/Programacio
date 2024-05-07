#Dissenya un algorisme corresponent a un programa que donada una frase acabada en punt,
#determini si té més caràcters “b” que “c”.
print("Dime una frase que contenga b o c y termine en .")
x = input("")
z = 0
y = 0
a = 0
for i in range(len(x)):
    caracter = x[i]
    if caracter == "b" or caracter == "B":
        y += 1
    elif caracter == "a" or caracter == "A":
        z += 1
    if caracter == ".":
        a = 1
if y > z and a == 1:
    print("B tiene más caracteres que A")
elif y < z and a == 1:
    print("B no tiene más caracteres que A")
elif y == z and a == 1:
    print("Tienen los mismos caracteres B que A")
elif y > z and a == 0:
    print("B tiene más caracteres que A, pero tendrías que haber puesto un '.'")
elif y < z and a == 0:
    print("B no tiene más caracteres que A, pero tendrías que haber puesto un '.'")
elif y == z and a == 0:
    print("Tienen los mismos caracteres B que A, pero tendrías que haber puesto un '.'")
else:
    print("ERROR")