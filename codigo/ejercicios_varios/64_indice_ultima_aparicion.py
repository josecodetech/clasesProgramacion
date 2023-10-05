# ¿Cómo encontrar el índice de la última aparición de un elemento en una lista?
lista = [1, 2, 2, 3, 3, 3, 4, 5]
elemento = 3
indice_ultima_aparicion = len(lista) - 1 - lista[::-1].index(elemento)
print(lista)
print(indice_ultima_aparicion) 