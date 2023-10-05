# ¿Cómo encontrar el segundo elemento más grande en una lista? 
lista = [5, 2, 8, 1, 3]
lista_ordenada = sorted(lista, reverse=True)
segundo_mas_grande = lista_ordenada[1]
print(lista)
print(lista_ordenada)
print(segundo_mas_grande)