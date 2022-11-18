from random import randint
def get_unique_list_numbers(start=-10,stop=10,size=15) -> list[int]:
    list_ = []
    while len(list_)<size:
        digit_ = randint(start,stop)
        if digit_ in list_:
            continue
        else:
            list_.append(digit_)
    return list_
        # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))



