bien = int(input("¿Cuantas respuestas ha acertado? "))
mal = int(input("¿Cuantas respuestas ha fallado? "))
vacio = int(input("¿Cuantas respuestas ha dejado vacío? "))
nota = print(f"La nota final es de: {(bien*5)+(mal*-1)+(vacio*0)}")