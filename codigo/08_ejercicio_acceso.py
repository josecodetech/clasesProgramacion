clave = 1234
usuario = 'jose' 
nombre_usuario = input("Dime el nombre de usuario para entrar -> ")
clave_usuario = int(input("Dime la clave -> "))
nombre_usuario = nombre_usuario.lower()
if nombre_usuario == usuario and clave_usuario == clave: # ver con or
    print("Puedes entrar")
else:
    print("No tienes permitido el acceso")
    