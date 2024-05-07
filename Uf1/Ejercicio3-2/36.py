#Algorisme que determini quina és la primera vocal que trobem en una frase acabada en punt.
print("Dime una frase")
x = input("")
z = 0
y = 0
a = 0
for i in range(len(x)):
    caracter = x[i]
    if caracter == "a" or caracter == "A" or caracter == "e" or caracter == "E" or caracter == "i" or caracter == "I" or caracter == "o" or caracter == "O" or caracter == "u" or caracter == "U":
        print(f"La primera vocal de la frase es {caracter}")
        break