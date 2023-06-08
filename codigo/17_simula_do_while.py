numero = 0
while True:
    numero = int(input("Ingresa un numero entre 1 y 10-> "))
    if numero >= 1 and numero <=10:
        break
    else:
        print("El numero debe ser entre 1 y 10")
print("Hemos terminado")