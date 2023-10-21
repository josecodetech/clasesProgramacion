# ¿Cómo contar la cantidad de elementos impares en una lista?
lista = [1, 2, 3, 4, 5]
impares = sum(1 for elemento in lista if elemento % 2 != 0)
print(lista)
print(impares)