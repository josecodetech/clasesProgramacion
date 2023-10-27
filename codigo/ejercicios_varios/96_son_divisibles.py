# ¿Cómo contar la cantidad de elementos en una lista que son divisibles por otro número?  
lista = [1, 2, 3, 4, 5]
divisibles_por_2 = sum(1 for elemento in lista if elemento % 2 == 0)
print(lista)
print("Hay", divisibles_por_2, "elementos divisibles por 2")
