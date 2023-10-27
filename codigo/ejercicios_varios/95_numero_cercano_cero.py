# ¿Cómo encontrar el número más cercano a cero en una lista?
lista = [5, 2, -8, 1, -3]
mas_cercano = min(lista, key=abs)
print(lista)
print("El numero mas cercano a cero es:", mas_cercano)