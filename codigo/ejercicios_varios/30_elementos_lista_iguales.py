# ¿Cómo verificar si todos los elementos de una lista son iguales?
lista = [1, 1, 1, 1, 1]
if all(elemento == lista[0] for elemento in lista):
    print("Todos los elementos son iguales")
else:
    print("No todos los elementos son iguales")