# ¿Cómo pasar los dígitos de un número a una lista?
num = 8723645
digitos = [int(d) for d in str(num)]
print(digitos)
print(type(digitos))