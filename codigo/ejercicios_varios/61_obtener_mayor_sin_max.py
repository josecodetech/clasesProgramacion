# ¿Cómo obtener el número más grande de una lista sin usar la función max()? 
lista = [5, 2, 8, 1, 3]
mayor = lista[0]
for elemento in lista:
    if elemento > mayor:
        mayor = elemento
print(lista)
print(mayor)