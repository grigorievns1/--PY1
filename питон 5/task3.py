def get_unique_list_numbers() -> list[int]:
    list_ = set()
    from random import randint
    while len(list_)!=15:
        list_.add(randint(-10,10))
    return [*list_]
        # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
