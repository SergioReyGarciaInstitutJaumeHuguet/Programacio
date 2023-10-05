# Escriure un programa que llegeixi un any indicar si és de traspàs. 
# Nota: un any és de traspàs si és un nombre divisible per 4, però no si és divisible per 100, 
# excepte que també sigui divisible per 400.

any = int(input("dies del any "))
if any % 4 ==0:
    if any % 100 !=0 or any % 400 ==0:
        print("es un any de traspas")
    else:
         print("no es un any de traspas ")
else:
    print("no es un any de traspas ")