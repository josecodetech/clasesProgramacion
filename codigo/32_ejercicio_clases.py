class Persona:
    identificador = 0
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        Persona.identificador += 1
class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad, carrera):
        super().__init__(nombre, apellidos, edad)
        self.carrera = carrera
        self.nota = None
        self.alta = False
    def poner_nota(self, nota):
        self.nota = nota
    def obtener_nota(self):
        if self.nota is not None:
            return self.nota
        else:
            return "No se ha asignado ninguna nota"
    def dar_alta(self):
        if self.alta:
            print("Ya estaba de alta")
        else:
            self.alta = True
    def obtener_alta(self):
        return self.alta
    def __str__(self):
        return f"Alumno: {self.nombre}, {self.apellidos} estudiando {self.carrera}"
alumno1 = Alumno("Jose","Ojeda",51,"Empresariales")
print(alumno1)
print(Persona.identificador)
alumno1.poner_nota(8.5)
alumno1.dar_alta()
print(alumno1.obtener_alta())
print(alumno1.obtener_nota())
alumno2 = Alumno("Maria","Sanchez", 48, "Biologia")
print(alumno2)
print(Persona.identificador)
