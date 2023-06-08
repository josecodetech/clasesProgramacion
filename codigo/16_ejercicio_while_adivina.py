numero_secreto = 56
adivinado = False
while not adivinado:
    intento = int(input("Adivina el numero secreto -> "))
    if intento == numero_secreto:
        print("Has acertado")
        adivinado = True
    else:
        print("Sigue probando")