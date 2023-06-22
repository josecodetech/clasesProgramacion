try:
    lista = [1,2,3,4]
    print(lista[6])
except IndexError:
    print(f"Indice fuera de rango")
except ValueError:
    print("Valor invalido")
    
try:
    num = int(input("Ingresa un numero: "))
    resultado = 10 / num
    print(resultado)
except Exception as e: 
    print(f"Error : {e}")
else:
    print("Estoy en el else")
finally:
    print("Esto se ejecuta siempre")