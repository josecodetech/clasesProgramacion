CONTACTOS_FICHERO = "contactos.txt"
def guardar_contacto(contacto):
    with open(CONTACTOS_FICHERO,"+a") as f:
        f.write(f"{contacto.nombre},{contacto.email},{contacto.telefono}")
        f.write("\n")
def listar_contactos():
    contactos = []
    try:
        with open(CONTACTOS_FICHERO,"r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos)==3:
                    nombre, email, telefono = datos
                    contactos.append((nombre, email, telefono))
    except FileNotFoundError:
        return []
    return contactos
