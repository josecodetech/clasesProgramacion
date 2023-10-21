# ¿Cómo verificar si una cadena es un número entero positivo?
cadena = "12345"
es_entero_positivo = cadena.isdigit() and int(cadena) > 0
print(cadena)
print(es_entero_positivo)