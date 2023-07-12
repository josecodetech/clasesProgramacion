from modulos.contacto import Contacto
from modulos.archivo import guardar_contacto, listar_contactos

def mostrar_menu():
    print("1. Listar contactos")
    print("2. Añadir contacto")
    print("3. Salir")
def listar_contactos_menu():
    print("*"*25)
    print("=== Lista de contactos ===")
    contactos = listar_contactos()
    if contactos:
        for contacto in contactos:
            print(contacto)
    else:
        print("No hay contactos disponibles")
    print("*"*25)
def añadir_contacto_menu():
    print("=== Añadir contacto ===")
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Telefono: ")
    nuevo_contacto = Contacto(nombre, email, telefono)
    guardar_contacto(nuevo_contacto)
    print("Contacto añadido correctamente")
def main():
    while True: 
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            listar_contactos_menu()
        elif opcion == "2":
            añadir_contacto_menu()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, prueba de nuevo")
if __name__ == "__main__":
    main()