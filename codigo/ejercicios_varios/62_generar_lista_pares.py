# ¿Cómo generar una lista de números pares en un rango dado?
inicio = 1
fin = 10
pares = [num for num in range(inicio, fin+1) if num % 2 == 0]
print(pares)