personas = {
    "Juan":25,
    "Maria":41,
    "Pedro":28
}
print(personas)
print(f'La edad de Maria es de {personas["Maria"]} años')

frutas = {
    "manzana":"rojo",
    "platano":"amarillo",
    "naranja":"naranja"
}
print(f'El color del platano es {frutas["platano"]}')

paises = {
    "España":"Madrid",
    "Francia":"Paris",
    "Italia":"Roma"
}
print(paises["Francia"])
print("*"*20)
print("Pais - Capital")
for pais,capital in paises.items():
    print(pais+" - "+capital)

ciudades = {
    "Madrid":320000,
    "Barcelona":310000,
    "Valencia": 290000,
    "Sevilla":240000
}  
poblacion_total = sum(ciudades.values())
print(f"La poblacion total es de {poblacion_total} habitantes")
print(ciudades['Sevilla'])
  