# creacion de la funcion
def saludar(nombre='Sin nombre'):
    print(f'Hola, {nombre}')
    
#nombre = input('Dime tu nombre -> ')
# llamada a la funcion
#saludar(nombre)

def sumar(num1=0, num2=0):
    resultado = num1 + num2
    return resultado
def multiplicar(num1,num2):
    return num1*num2
def media(numeros):
    suma = sum(numeros)             
    media = suma / len(numeros)         
    return media
# llamadas
texto = f'El resultado obtenido es {sumar(1,8)}'
print(texto)
multiplicacion = multiplicar(4,5)
print("El resultado de la multiplicacion es",multiplicacion)
lista_numeros = [4,5,63,2,1,6,4,9]
media = media(lista_numeros)
print(f'La media de la lista de numeros es {media}')
