# ¿Cómo calcular el área de un polígono regular?
import math
lado = 5
num_lados = 6
apotema = lado / (2 * math.tan(math.pi / num_lados))
area = (num_lados * lado * apotema) / 2
print(area)