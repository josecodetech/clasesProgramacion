pares = []
for numero in range(1,101):
    if numero % 2 == 0:
        pares.append(numero)
        print(f"El numero {numero} es par")
print("Hemos terminado de recorrer el rango dado")
print(pares)
for par in pares:
    print(par)