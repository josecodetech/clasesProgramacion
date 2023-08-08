# ¿Cómo reemplazar un elemento en una lista?
lista = [1, 2, 3, 4, 5]
print(lista)
elemento_viejo = 3
elemento_nuevo = 6
indice = lista.index(elemento_viejo)
lista[indice] = elemento_nuevo
print(lista)