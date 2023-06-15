def menu():
    print('*'*30)
    print("1 Sumar\n2 Restar\n3 Multiplicar\n4 Dividir\n5 Salir")
    print('*'*30)
    opcion = int(input('-> '))
    return opcion
def solicitar_numeros():
    num1 = int(input('Ingresa el primer numero: '))
    num2 = int(input('Ingresa el segundo numero '))
    return num1, num2
def calcular(opcion=1,num1=0,num2=0):
    if (opcion==1):
        resultado = num1 + num2
    elif (opcion==2):
        resultado = num1 - num2
    elif (opcion==3):
        resultado = num1 * num2
    elif (opcion==4):
        resultado = num1 / num2
    else:
        resultado = None
    return resultado
if __name__=='__main__':
    while True:
        opcion = menu()
        if opcion>=1 and opcion<5:
            num1, num2 = solicitar_numeros()
            resultado = calcular(opcion,num1,num2)
            print(f'El resultado de la operacion es {resultado}')
        elif opcion==5:
            print("Hasta pronto!!!")
            exit()
        else:
            print('Marca una opcion valida')