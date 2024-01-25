parc1 = float(input("Nota de tu primera parcial: "))
parc2 = float(input("Nota de tu segunda parcial: "))
parc3 = float(input("Nota de tu tercera parcial: "))
parcMed = (parc1+parc2+parc3)/3
parciales = ((parcMed)*55)/100
efin = float(input("Nota de tu examen final: "))
exfin = ((efin*30)/100)
tfin = float(input("Nota de tu trabajo final: "))
trfin = ((tfin*15)/100)
res = (parciales+exfin+trfin)
print(f"La nota final es es {res}")