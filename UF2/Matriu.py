import random
letra = 0
a = []
for i in range(7):
    letra += random.choice(1,2,3,4,5,6,7)
for i in range(7):
    a.append([letra]*7)
print(a)