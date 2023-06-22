# r
# w
# a
# r+
# Creacion y escritura
try:
    with open('fichero.txt','w') as f:
        f.write("Hola, estoy escribiendo en el fichero de texto desde python\nAdios.")
except IOError:
    print("No se pudo escribir en el fichero")
# Añadir
try:
    with open('fichero.txt','a') as f:
        f.write("\nAñadiendo mas contenido al final del fichero.")
except IOError:
    print("No se pudo añadir el contenido")
# Lectura
try:
    with open('fichero.txt','r') as f:
        contenido = f.read()
        print(contenido)
        # no hace falta en el with f.close()
except FileNotFoundError:
    print("Error: fichero no encontrado")