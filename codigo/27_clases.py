class Persona:
    def __init__(self,nombre,edad:int):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, {self.nombre} y tengo {self.edad} años")
    def __str__(self):
        return (f"Soy un objeto llamado {self.nombre} de la clase persona")
    
if __name__=='__main__':
    persona01 = Persona("Jose",51)
    persona02 = Persona("Maria",48)
    persona01.saludar()
    persona02.saludar()
    print(persona01.nombre)
    print(persona01)
    #persona01.devolver_nombre()