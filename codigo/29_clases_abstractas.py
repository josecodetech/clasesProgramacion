class Figura:
    def calcular_area(self):
        raise NotImplementedError("Metodo no implementado")
class Rectangulo(Figura):
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    def calcular_area(self):        
        return self.base * self.altura

if __name__=='__main__':
    figurita = Rectangulo(15,5)
    print(figurita.calcular_area())