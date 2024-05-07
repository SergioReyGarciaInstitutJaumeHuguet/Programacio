import random
matrix = [[" " for i in range(6)]for i in range(5)]
for i in range(5): #Lleno la matriz con lo que me pedía el ejercicio
    for j in range(6):
        matrix[i][j] = (((i+1)*10)-(j))+6 
        #Primera vuelta: i+1 = 1*10 = 10-0 = 10+6 = 16
        #Segunda vuelta: i+1 = 1*10 = 10-1 = 9+6 = 15

def creaVector():
    c = 0 #Voy a usar a, b, c para sumar. A para tener el número actual, b para sumar la segunda posición y c para sumar la primera suma de la primera posición mas la segunda posició, con todas las otras posiciónes
    vector = []
    for i in range(5):
        for j in range(6):
            a = matrix[i][j]
            if j > 1:
                c = a + c
            elif j > 0:
                c = a + b
            b = a
        vector.append(c)
    print(f"Vector: {vector}\n")

def posaZerosParells():
    for i in range(5):
        for j in range(6):
            if j % 2 == 0: #Si el resto de la división es 0, es parejo
                matrix[i][j] = 0
    print(f"posar a 0 parells: {matrix}\n")

def vectorAleatori():
    numsAleatori = []
    nums = []
    for i in range(80): #añado 20 números a una lista
        i+=1
        if i < 5: #Verifico que sea mayor que 5
            continue
        else:
            nums.append(i)
    for i in range(7):
        numsAleatori.append(random.choice(nums)) #Inserto el número random
    return numsAleatori

def sumar(h):
    c = 0 #Uso la mísma lógica que usé en el creaVector(), pero ahora importando la lista que quiero sumar
    for i in h:
        a = i
        if j > 1:
            c = a + c
        elif j > 0:
            c = a + b
        b = a
    return c

creaVector()
posaZerosParells()
print(f"Vector aleatori: {sumar(vectorAleatori())}\n")