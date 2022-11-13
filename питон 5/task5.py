
def get_random_password(n=8) -> str:
    import random
    str_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return random.sample(str_, n)

     # TODO написать функцию генерации случайных паролей


print(''.join(get_random_password()))
