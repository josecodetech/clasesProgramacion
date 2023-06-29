class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __len__(self):
        return 2 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
if __name__=='__main__':
    punto01 = Punto(5,6)
    punto02 = Punto(2,1)
    print(punto01)
    print(punto02)
    print(len(punto01))
    print(len(punto02))
    print(punto01 == punto02)