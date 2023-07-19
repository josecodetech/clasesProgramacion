#¿Cómo verificar si una cadena es un palíndromo?
cadena = "anita lava la tina"
cadena = cadena.lower()
cadena = cadena.replace(" ","")
if cadena == cadena[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")