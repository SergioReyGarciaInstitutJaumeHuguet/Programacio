HoraSemana = int(input("¿Cuantas horas trabajas a la semana?"))
HoraPrecio = int(input("¿A cuanto cobras la hora?"))
x = HoraSemana
y = 1
if HoraSemana > 40:
    x = HoraSemana - 40
    y = x * (HoraSemana*1.5)
    HoraSemana = (HoraSemana * HoraPrecio) + y
else:
    HoraSemana = HoraSemana * HoraPrecio

print(f"Cobrarás a la semana {HoraSemana}€")