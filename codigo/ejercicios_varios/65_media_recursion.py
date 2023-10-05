# ¿Cómo calcular el promedio de una lista de números usando recursión?  
def promedio(lista):
    if not lista:
        return 0
    else:
        return sum(lista) / len(lista)
lista = [1, 2, 3, 4, 5]
print(lista)
promedio_lista = promedio(lista)
print(promedio_lista)