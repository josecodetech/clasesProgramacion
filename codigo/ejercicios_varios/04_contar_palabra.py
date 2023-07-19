#¿Cómo contar la frecuencia de palabras en una cadena?
cadena = "La vida es bella y bella es la vida"
cadena=cadena.lower()
palabras = cadena.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print(frecuencia) 
        
        