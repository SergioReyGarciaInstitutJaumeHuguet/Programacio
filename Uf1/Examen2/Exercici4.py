Renos = {
    "1": {
        "Nom": "Rudolph",
        "Edat": 8,
        "Nas vermell": "True"
    },
    "2": {
        "Nom": "Dancer",
        "Edat": 7,
        "Nas vermell": "False"
    },
    "3": {
        "Nom": "Blitzen",
        "Edat": 6,
        "Nas vermell": "True"
    }
}
for i in Renos:
    Renos[i]["Vitalitat"] = Renos[i]["Edat"]
    if Renos[i]["Nas vermell"] == "True":
        Renos[i]["Vitalitat"] += 1
    print(Renos[i])
print("***RENOS CON LA NARIZ ROJA Y MAS DE 7 AÑOS***")
for i in Renos:
    if Renos[i]["Nas vermell"] == "True" and Renos[i]["Edat"] > 7:
        print(Renos[i])