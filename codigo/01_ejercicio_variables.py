nombre = input("Dime tu nombre -> ")
apellido = input("Dime tu apellido -> ")
edad = int(input("Dime tu edad -> "))
persona = {
    'Nombre':nombre,
    'Apellido':apellido,
    'Edad':edad
}
print(persona['Nombre'])
print(persona['Apellido'])
print(persona['Edad'])
print(persona.keys())
print(persona.values())