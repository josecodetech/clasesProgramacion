# ¿Cómo calcular el área de un triángulo dado los lados?
import math
lado1 = 5
lado2 = 4
lado3 = 3
semiperimetro = (lado1 + lado2 + lado3) / 2
area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
print(area)