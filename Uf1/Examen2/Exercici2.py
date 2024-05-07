vuelta = 0
piramide = []
for i in range(13):
    piramide.append(" ")
for i in range(7):
    vuelta += 1
    if vuelta == 1:
        del(piramide[7])
        piramide.insert(7,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 2:
        del(piramide[6])
        del(piramide[8])
        piramide.insert(6,"^")
        piramide.insert(8,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 3:
        del(piramide[5])
        del(piramide[9])
        piramide.insert(5,"^")
        piramide.insert(9,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 4:
        del(piramide[4])
        del(piramide[10])
        piramide.insert(4,"^")
        piramide.insert(10,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 5:
        del(piramide[3])
        del(piramide[11])
        piramide.insert(3,"^")
        piramide.insert(11,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 6:
        del(piramide[2])
        piramide.insert(2,"^")
        del(piramide[12])
        piramide.insert(12,"^")
        for i in piramide:
            print(i, end="")
        print("")
    elif vuelta == 7:
        del(piramide[1])
        piramide.insert(1,"^")
        piramide.insert(13,"^")
        for i in piramide:
            print(i, end="")
        print("")