# ¿Cómo obtener la sublista de una lista que cumple cierta condición?
lista = [1, 2, 3, 4, 5,6,9,12]
sublista = [elemento for elemento in lista if elemento > 3]
print(lista)
print(sublista)