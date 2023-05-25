# crear diccionario
diccionario = {}
print(type(diccionario))
diccionario = {"clave1":"valor1","clave2":235,"bool":True}
print(diccionario)
mi_diccionario = {"nombre":"Juan","edad":25,"ciudad":"Madrid"}
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])
mi_diccionario["apellidos"]='Ojeda'
print("*"*25)
print(mi_diccionario)
print("Claves")
print(mi_diccionario.keys())
print("Valores")
print(mi_diccionario.values())
print(mi_diccionario.items())
print("*"*25)
mi_diccionario["edad"]="mi edad"
print(mi_diccionario)
del mi_diccionario['apellidos']
# este borra todo el diccionario y su referencia
# del mi_diccionario
print(mi_diccionario)
# este limpia datos pero no borra
mi_diccionario.clear()
print(mi_diccionario)