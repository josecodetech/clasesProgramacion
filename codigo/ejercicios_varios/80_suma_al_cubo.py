# ¿Cómo calcular la suma de los dígitos al cubo de un número?
num = 12345
suma_cubos = sum(int(digit) ** 3 for digit in str(num))
print(num)
print(suma_cubos) 