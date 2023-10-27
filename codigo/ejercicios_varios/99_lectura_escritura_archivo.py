# escritura
with open("ejemplo.txt", "w") as f: 
    f.write("Hola, este es un ejemplo de escritura en fichero de texto con python\n")

# lectura
with open("ejemplo.txt", "r") as f: 
    contenido = f.read() 
    print(contenido)