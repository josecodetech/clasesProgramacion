# ¿Cómo calcular el factorial de un número usando recursión?
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = 5
factorial_num = factorial(num)
print(factorial_num) 