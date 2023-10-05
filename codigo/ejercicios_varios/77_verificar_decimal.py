# ¿Cómo verificar si una cadena es un número decimal?
cadena = "3.14"
es_decimal = cadena.replace(".", "", 1).isdigit()
print(cadena)
print(es_decimal)
