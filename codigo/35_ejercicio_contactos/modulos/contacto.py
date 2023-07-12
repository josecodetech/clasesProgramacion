class Contacto:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Telefono: {self.telefono}"
    