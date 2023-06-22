try:
    with open('fichero.txt','r') as f:
        lineas = f.readlines()
        for linea in lineas:
            print(linea)
except FileNotFoundError:
    print("Fichero no encontrado")
    