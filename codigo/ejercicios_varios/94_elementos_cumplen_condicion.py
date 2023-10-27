#  ¿Cómo contar la cantidad de elementos en una lista que cumplen una condición? 
lista = [1, 2, 3, 4, 5, 6, 7, 8]
cantidad = sum(1 for elemento in lista if elemento > 3)
print(lista)
print("La cantidad de elementos es:", cantidad)