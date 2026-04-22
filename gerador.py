import random
import string
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=12))
print(senha)