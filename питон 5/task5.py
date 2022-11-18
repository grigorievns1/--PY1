import string
import random
def get_random_password(n=8) -> str:
    str_ = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.sample(str_, n)

     # TODO написать функцию генерации случайных паролей


print(''.join(get_random_password()))
