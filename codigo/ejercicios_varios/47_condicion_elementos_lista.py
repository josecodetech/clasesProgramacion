# ¿Cómo verificar si todos los elementos de una lista cumplen una condición? 
lista = [1, 2, 3, 4, 5]
if all(elemento > 0 for elemento in lista):
    print("Todos los elementos cumplen la condición")
else:
    print("No todos los elementos cumplen la condición")