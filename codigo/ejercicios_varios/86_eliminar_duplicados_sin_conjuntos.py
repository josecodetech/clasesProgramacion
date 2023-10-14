# ¿Cómo eliminar elementos duplicados de una lista sin usar conjuntos?
lista = [1, 2, 2, 3, 3, 3, 4, 5]
lista_sin_duplicados = []
for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(lista)    
print(lista_sin_duplicados)