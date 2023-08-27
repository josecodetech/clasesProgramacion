# ¿Cómo calcular la suma de los dígitos de un número?
num = 12345
suma_digitos = sum(int(d) for d in str(num))
print(suma_digitos)