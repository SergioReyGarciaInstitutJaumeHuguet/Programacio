eur2 = int(input("Dime los dos euros: "))
eur1 = int(input("Dime los euros: "))
cent50 = int(input("Dime los centimos de 50: "))
cent20 = int(input("Dime los centimos de 20: "))
cent10 = int(input("Dime los centimos de 10: "))
tot = ((((eur2*2)+eur1)*100)+(cent50*50)+(cent20*20)+(cent10*10))
Euros = tot // 100
Centimos = tot % 100
print(f"Tienes {Euros} euros y {Centimos} centimos")