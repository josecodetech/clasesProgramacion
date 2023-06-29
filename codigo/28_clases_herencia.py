class Persona:
    def __init__(self,nombre,edad:int):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, {self.nombre} y tengo {self.edad} años")
class Estudiante(Persona):
    def __init__(self, nombre, edad: int, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    def estudiar(self):
        print(f"Soy estudiante de {self.carrera}")
if __name__=='__main__':
    estudiante01 = Estudiante("Jose",51,"Empresariales")
    estudiante02 = Estudiante("Maria",48,"Biologia")
    estudiante01.saludar()
    estudiante02.saludar()
    estudiante01.estudiar()
    estudiante02.estudiar()