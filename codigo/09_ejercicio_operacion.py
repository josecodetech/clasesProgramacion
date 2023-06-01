operacion = input("Quieres sumar (s) o restar (r)? -> ")
operacion = operacion.lower()
num1 = int(input("Dime el primer numero -> "))
num2 = int(input("Dime el segundo numero -> "))
if operacion == "s":
    print("Sumando dos numeros")
    print(f"El resultado de sumar {num1}+{num2} es {num1+num2}")
elif operacion == "r":
    print("Restando dos numeros")
    print(f"El resultado de restar {num1}-{num2} es {num1-num2}") 
else:
    print("Operacion no valida")       