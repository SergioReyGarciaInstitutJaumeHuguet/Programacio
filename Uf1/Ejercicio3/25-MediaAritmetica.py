num = 0
x = 0
y = 0
z = 70000
while num != z:
    x = int(input("Ingresa un valor: "))
    if x == 0:
        z = num
        continue
    else:
        num += 1
        y = y + x
        y = y/num
        z = num+z
print(y)