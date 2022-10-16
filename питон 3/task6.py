list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
for m in range(len(list_numbers)):
    max_hight = list_numbers[max_index]
    chel = list_numbers[m]
    if chel > max_hight:
        max_index = m
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]
# TODO Оформить решение

print(list_numbers)
