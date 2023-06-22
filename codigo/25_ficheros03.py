try:
    with open('fichero.txt','r') as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("Fichero no encontrado")
except PermissionError:
    print("No tienes permiso sobre este fichero")
