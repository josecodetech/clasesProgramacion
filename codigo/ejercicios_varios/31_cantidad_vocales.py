# ¿Cómo contar la cantidad de vocales en una cadena?
cadena = "Hola, mundo!"
vocales = sum(1 for char in cadena if char.lower() in 'aeiou')
print(vocales)