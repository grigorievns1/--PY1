def get_count_char(str_):
    dict_ = {}
    str_ = "".join(c for c in str_.lower() if c.isalpha())
    for letter in str_:
        dict_[letter] = dict_.get(letter,0) + 1
    return dict_
            # TODO посчитать количество каждой буквы в строке в аргументе str_
def get_share_char(get_count_char):
    char_in_percent = {}
    total = sum(get_count_char.values())
    for char,value in get_count_char.items():
        char_in_percent[char] = round(value/total*100,1)
    return char_in_percent



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_share_char(get_count_char(main_str)))
print(sum(get_share_char(get_count_char(main_str)).values()))