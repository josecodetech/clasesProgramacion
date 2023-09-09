# ¿Cómo verificar si una cadena es un palíndromo sin considerar mayúsculas y minúsculas?
cadena = "Anita lava la tina"
cadena_sin_espacios = cadena.replace(" ", "").lower()
es_palindromo = cadena_sin_espacios == cadena_sin_espacios[::-1]
print(es_palindromo)