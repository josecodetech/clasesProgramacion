#¿Cómo verificar si una lista está ordenada de forma descendente?
lista = [5, 4, 3, 2, 1]
print(lista)
es_descendente = lista == sorted(lista, reverse=True)
print(es_descendente)