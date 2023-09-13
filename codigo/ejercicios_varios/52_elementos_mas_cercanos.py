# ¿Cómo encontrar el elemento de una lista más cercano a un valor dado?
lista = [1, 2, 3, 4, 5]
valor = 3.7
elemento_cercano = min(lista, key=lambda x: abs(x - valor))
print(lista)
print(elemento_cercano)