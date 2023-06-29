class Coche:
    contador = 0
    def __init__(self,marca):
        self.marca = marca
        Coche.contador += 1 # contador = contador + 1
    @classmethod
    def obtener_cantidad(cls):
        return cls.contador
if __name__=='__main__':
    coche1 = Coche("Ford")
    coche2 = Coche("Toyota")
    coche3 = Coche("Seat")
    coche4 = Coche("Kia")
    print(Coche.obtener_cantidad())