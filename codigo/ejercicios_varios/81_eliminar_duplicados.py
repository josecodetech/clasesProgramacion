# ¿Cómo eliminar elementos duplicados de una lista manteniendo el orden original usando un conjunto auxiliar?
lista = [1, 2, 2, 3, 3, 3, 4, 5]
lista_sin_duplicados = []
conjunto_auxiliar = set()
for elemento in lista:
    if elemento not in conjunto_auxiliar:
        lista_sin_duplicados.append(elemento)
    conjunto_auxiliar.add(elemento)
print(lista)
print(lista_sin_duplicados)