# ¿Cómo eliminar elementos repetidos de una lista manteniendo el orden original?
lista = [1, 2, 2, 3, 3, 3, 4, 5]
lista_sin_repetidos = []
for elemento in lista:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)
print(lista)
print(lista_sin_repetidos)