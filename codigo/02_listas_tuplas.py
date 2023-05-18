# listas
lista_vacia = []
print(type(lista_vacia))
numeros = [1,5,3,4,5]
palabras = ['Hola','Mundo','Python']
print(numeros[2])
print(palabras[0])
print(palabras)
palabras[1]='2356'
print(palabras)
palabras.append('Añadida')
print(palabras)
lista01 = [1,2,3]
lista02 = [4,5,6]
lista03 = lista01+lista02
print(lista03)
palabras.sort()
print(palabras)
lista01.append(5)
print(lista01)
lista01.extend(lista02)
print(lista01)
del lista01[2] #borra el elemento por su indice
print(lista01)
lista01.remove(4) #borra por valor
print(lista01)
lista01.insert(3,1012)
print(lista01)

# tuplas
coordenadas = (3.14, 2.71)
colores = ('rojo','verde','amarillo')
numeros = (1,2,3,56,3)
print(type(numeros))
print(colores)
print(colores[2])
tupla01=(1,3,5)
tupla02=(8,3,9)
# union o combinacion de tupla
tupla03=tupla01+tupla02
print(tupla03)
# tupla03[4]=56 LA TUPLA ES INMUTABLE
print(tupla01[2])
print(tupla02[1])
tupla = (10,32,65)
print(tupla)
print(type(tupla))
# desempaquetar tupla
a, b, c = tupla
print(a)
print(b)
print(c)
suma = a+b+c
print(suma)
print(type(palabras))
tupla_palabras = tuple(palabras)
print(type(tupla_palabras))
print(tupla_palabras)
nombre = 'Jose'
print(type(nombre))
print(nombre)
lista_nombre = list(nombre)
print(type(lista_nombre))
print(lista_nombre)
