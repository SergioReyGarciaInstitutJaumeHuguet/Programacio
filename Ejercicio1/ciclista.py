Hora = int(input("Introdueix les hores de sortida (0-23):"))
Minuts = int(input("Introdueix els minuts de sortida (0-59): "))
Segons = int(input("Introdueix els segons de sortida (0-59): "))
T = int(input("Introdueix el temps de viatge en segons"))
Segons_Sortida = Hora * 3600 + Minuts * 60 + Segons
Segons_Arribada = Segons_Sortida + T 
Hora_arribada = Segons_Arribada //3600
Segons_Arribada %= 3600
min_arribada = Segons_Arribada // 60
segons_nous = Segons_Arribada %  60
print (f"Aques es la hora a la que arriabra: {Hora_arribada:02} {min_arribada:02} {segons_nous:02}")