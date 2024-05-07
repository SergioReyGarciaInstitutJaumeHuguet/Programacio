def llenar():
    global b
    global c
    if b >= 1:
        b = -1
        c += 1
        if c > 1:
            c = 0
    b += 1
b = 0
c = 0
matrix = [[" " for i in range(2)]for i in range(2)]
matrix2 = [[" " for i in range(2)]for i in range(2)]
matrix3 = [[" " for i in range(2)]for i in range(2)]

for i in range(8):
    while True:
        num = input(f"Dime 1 número ({8-i} números restants): ")
        if num.isdigit():
            num = int(num)
            break
        else:("Solo números")
    if i < 4:
        matrix[c][b] = num
        llenar()
    else:
        matrix2[c][b] = num
        llenar()

for i in range(4):
    matrix3[b][c] = matrix[b][c]*matrix2[b][c]
    llenar()

print(matrix)
print(matrix2)
print(matrix3)