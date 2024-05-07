final = False
frutasPrecio = {
    'manzana': 1,
    'pera': 0.50,
    'platano': 1.20
}
while final == False:
    frutas = input('Dime una fruta: ')
    if frutas not in frutasPrecio: 
        print(f"Error. La fruta {frutas} no existe")
        break
    cantidad = int(input('Dime la cantidad: '))
    print(frutasPrecio[frutas] * cantidad)
    finalPregunta = input("Pulsa 1 si quieres continuar")
    if finalPregunta != '1':
        final = True