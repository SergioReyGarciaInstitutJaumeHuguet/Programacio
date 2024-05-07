num1 = 1
num =0
contador = 0
while num1 !=0:
    num1= int(input('numero'))
    if num1 %2 !=0:
        contador +=1
        if contador >=6:
            continue
        num+=num1
    else:
        continue
print(num)

