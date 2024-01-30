def liebre(n):
    if n == 0:
        return 2
    elif n == 1:
        return 4
    else:
        return (liebre(n-2)+liebre(n-1))
n=int(input("Meses que quieres saber: "))
for i in range(n):
    print(f"Mes {i}", end=" ")
print()
for i in range(0,n):
    print(liebre(i), end=(" "))