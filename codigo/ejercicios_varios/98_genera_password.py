import string
import random

letras = string.ascii_letters + string.digits
password = ''.join(random.choice(letras) for i in range(20))
print(password)