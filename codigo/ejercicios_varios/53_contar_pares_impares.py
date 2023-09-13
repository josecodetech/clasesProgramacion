# ¿Cómo contar la cantidad de elementos pares e impares en una lista?
lista = [1, 2, 3, 4, 5]
pares = sum(1 for elemento in lista if elemento % 2 == 0)
impares = sum(1 for elemento in lista if elemento % 2 != 0)
print("Lista: ", lista)
print("Pares: ", pares)
print("Impares: ", impares)