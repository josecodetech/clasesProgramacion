# ¿Cómo calcular la suma de los dígitos al cuadrado de un número?
num = 12345
suma_cuadrados = sum(int(digit) ** 2 for digit in str(num))
print(suma_cuadrados)